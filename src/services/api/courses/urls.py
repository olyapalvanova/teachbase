from django.urls import path

from services.api.courses.views import CourseListView, CourseDetailView

app_name = 'users'

urlpatterns = [
    path('', CourseListView.as_view(), name='list'),
    path('<int:pk>', CourseDetailView.as_view(), name='detail'),
]
