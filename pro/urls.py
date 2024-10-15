from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('personal_details/', views.personal_details, name='personal_details'),
    path('coding_profiles/', views.coding_profiles, name='coding_profiles'),
    path('resume/', views.resume, name='resume'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('certifications/', views.certifications, name='certifications'),
    path('internships/', views.internships, name='internships'),
    path('co_curricular/', views.co_curricular, name='co_curricular'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





