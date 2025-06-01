from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/reportincident/', views.reportincident_view, name='reportincident'),
    path('dashboard/contactauthorities/', views.contactauthorities_view, name='contactauthorities'),
    path('dashboard/guidelines/', views.guidelines_view, name='guidelines'),
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('admin-dashboard/livemonitoring/', views.livemonitoring_view, name='livemonitoring'),
    path('admin-dashboard/alerts/', views.alerts_view, name='alerts'),
    path('admin-dashboard/analysis/', views.analysis_view, name='analysis'),
    path('features/', views.features_view, name='features'),
    path('howitswork/', views.howitswork_view, name='howitswork'),
    path('contact/', views.contact_view, name='contact'),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
