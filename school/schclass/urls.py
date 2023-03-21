from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('journal/', views.JournalApiView.as_view()),
    path('journal/<int:pk>/', views.SingleJournalView.as_view()),
    path('student/', views.StudentApiView.as_view()),
    path('student/<int:pk>/', views.SingleStudentView.as_view()),
    path('lessons/', views.LessonApiView.as_view()),
    path('lessons/<int:pk>/', views.SingleLessonView.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]