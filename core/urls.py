from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('contact/', views.contact, name='contact'),
    path('course/<str:course_slug>/', views.course_detail, name='course_detail'),
    
    path('change-language/<str:language_code>/', views.change_language, name='change_language'),
    path('test-language/', views.test_language, name='test_language'),
    
]