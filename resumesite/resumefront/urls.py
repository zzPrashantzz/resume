from django.urls import path
from django.contrib.auth import views as auth_views  
from . import views

urlpatterns = [
    # Authentication paths
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    
    # Basic pages
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Resume CRUD paths
    path('resume/create/', views.ResumeCreateView.as_view(), name='resume_create'),
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume_detail'),
    path('resume/<int:pk>/edit/', views.resume_edit, name='resume_edit'),
    path('resume/<int:pk>/delete/', views.ResumeDeleteView.as_view(), name='resume_delete'),

    path('resume/<int:resume_id>/enhance/', views.enhance_summary, name='enhance_summary'),
    
    # Section management paths
    path('resume/<int:pk>/<str:section_type>/add/', views.section_add, name='section_add'),
    path('resume/<int:pk>/<str:section_type>/<int:section_id>/edit/', 
         views.section_edit, name='section_edit'),
    path('resume/<int:pk>/<str:section_type>/<int:section_id>/delete/', 
         views.section_delete, name='section_delete'),
    
    # AI features paths
    path('resume/import/', views.resume_import, name='resume_import'),
    path('resume/ai-generate/', views.ai_generate, name='ai_generate'),
]