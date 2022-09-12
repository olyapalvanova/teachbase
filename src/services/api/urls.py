from django.urls import include, path

from services.api.courses import urls as course_urls

app_name = 'api'

urlpatterns = [
    path('courses/', include((course_urls.urlpatterns, course_urls.app_name), namespace='course')),  # noqa: E501
]
