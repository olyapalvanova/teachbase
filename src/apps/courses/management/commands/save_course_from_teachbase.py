import logging

from django.core.management import BaseCommand

from apps.teachbase.client import TeachBaseAPIClient
from services.api.courses.serializers import CourseSerializer


# Get an instance of a logger
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Save course in model `Course` from Teachbase'

    def handle(self, *args, **options):
        teach_base = TeachBaseAPIClient()
        teach_base.authorization()
        courses = teach_base.get_list_courses()
        serializer = CourseSerializer(data=courses, many=True)
        serializer.is_valid()
        if serializer.errors:
            logger.debug(serializer.errors)
        serializer.save()
