from django.urls import path

from core.erp.views.dashboard.views import *



app_name = 'erp'

urlpatterns = [
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    
]
