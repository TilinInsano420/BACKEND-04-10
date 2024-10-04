
from django.contrib import admin
from django.urls import path
from app.views import employeeData
from app.views import userRegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',employeeData),
    path('a',userRegistrationView)
    ]
