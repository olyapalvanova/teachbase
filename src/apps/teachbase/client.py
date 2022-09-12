import logging

import requests
from django.conf import settings


# Get an instance of a logger
logger = logging.getLogger(__name__)


class TeachBaseAPIClient:
    URL_TEACH_BASE = 'https://go.teachbase.ru/'
    GET_ACCESS_TOKEN = 'oauth/token'
    GET_ACCOUNT = 'endpoint/v1/account/settings'
    GET_LIST_COURSES = 'endpoint/v1/courses'
    GET_COURSE = 'endpoint/v1/courses/{0}'
    USER_CREATE = 'endpoint/v1/users/create'
    USER_REGISTER_SESSION = 'endpoint/v1/course_sessions/{0}/register'
    GET_LIST_COURSE_SESSIONS = 'endpoint/v1/courses/{0}/course_sessions'

    def __init__(self):
        self.access_token = None

    def authorization(self):
        payload = {'client_id': settings.CLIENT_ID,
                   'client_secret': settings.CLIENT_SECRET,
                   'grant_type': 'client_credentials'
                   }
        response = requests.post(
            self.URL_TEACH_BASE + self.GET_ACCESS_TOKEN, data=payload
        )
        data = response.json()
        if response.ok:
            self.access_token = data['access_token']
            return data
        msg = 'Problem with api `{0}`: {1}'.format(self.GET_ACCESS_TOKEN, data)
        logger.error(msg)

    @classmethod
    def is_valid_token(cls, token: str):
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        response = requests.get(
            cls.URL_TEACH_BASE + cls.GET_ACCOUNT, headers=headers
        )
        return response.ok

    def get_data(self, response, api):
        data = response.json()
        if response.ok:
            return data
        msg = 'Problem with api `{0}`: {1}'.format(api, data)
        logger.error(msg)

    def create_user(self, data: dict):
        headers = {'Authorization': 'Bearer {0}'.format(self.access_token)}
        response = requests.post(
            self.URL_TEACH_BASE + self.USER_CREATE, headers=headers, json=data
        )
        return self.get_data(response, self.USER_CREATE)

    def get_list_courses(self):
        headers = {'Authorization': 'Bearer {0}'.format(self.access_token)}
        response = requests.get(
            self.URL_TEACH_BASE + self.GET_LIST_COURSES, headers=headers
        )
        return self.get_data(response, self.GET_LIST_COURSES)

    def get_course(self, course_id):
        headers = {'Authorization': 'Bearer {0}'.format(self.access_token)}
        response = requests.get(
            self.URL_TEACH_BASE + self.GET_COURSE.format(course_id),
            headers=headers
        )
        return self.get_data(response, self.GET_LIST_COURSES)

    def get_list_course_sessions(self, course_id):
        headers = {'Authorization': 'Bearer {0}'.format(self.access_token)}
        response = requests.get(
            self.URL_TEACH_BASE + self.GET_COURSE.format(course_id),
            headers=headers
        )
        return self.get_data(response, self.GET_LIST_COURSE_SESSIONS)

    def register_user_course(self, session_id, data: dict):
        headers = {'Authorization': 'Bearer {0}'.format(self.access_token)}
        response = requests.post(
            self.URL_TEACH_BASE + self.USER_REGISTER_SESSION.format(session_id),
            headers=headers, json=data
        )
        return self.get_data(response, self.USER_CREATE)
