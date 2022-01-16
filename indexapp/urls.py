from django.urls import path
from . import views, xlsxtemplate, rca, gliit, tfcc, ci, svi, contact

urlpatterns = [
    path('', views.home, name='home'),
    path('create-template/', xlsxtemplate.CreateTemplate, name='template'),
    path('rca/', rca.OnlyRCA, name='rca'),
    path('gliit/', gliit.OnlyGLIIT, name='gliit'),
    path('tfcc/', tfcc.OnlyTFCC, name='tfcc'),
    path('ci/', ci.OnlyCI, name='ci'),
    path('all/', svi.allINDEXES, name='all'),
    path('about/', views.about, name='about'),
    path('contact/', contact.contact, name='contact'),
    path('message_sent/', contact.poruka_poslana, name='message_sent'),
]
