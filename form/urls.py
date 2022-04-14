"""norm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.NormFormPage.as_view(), name='form'),
    path('index.html', views.NormFormPage.as_view(), name='index'),
    path('<int:pk>', views.NormFormPage.as_view(), name='index'),
    path('get_pdf/<int:pk>', views.get_pdf_page, name='get_pdf_page'),
    path('form/', views.NormFormPage.as_view(), name='form'),
    path('submit_form', views.SubmitNormForm.as_view(), name='submit_form'),
    path('view_norm_forms', views.ViewNormFormsPage.as_view(), name='view_norm_forms'),
    path('api/v1/subjective_boilerplate_option', views.get_subjective_boilerplate_option_text, name='subjective_boilerplate_option'),
    path('api/v1/subjective_option', views.get_subjective_option_text, name='subjective_option'),
    path('api/v1/discussion_treatment_option', views.get_discussion_treatment_option_text, name='discussion_treatment_option'),
]
