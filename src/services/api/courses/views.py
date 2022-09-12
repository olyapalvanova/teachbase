from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.courses.models import Course
from services.api.courses.serializers import CourseSerializer


class CourseListView(ListAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class CourseDetailView(RetrieveAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
