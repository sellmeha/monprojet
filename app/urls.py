from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name="contact"),
    path('subjects/', subjects, name="subjects"),
    path('teachers/', teachers, name="teachers"),
    path('managers/', managers, name="managers"),
    path('etabs/', etablissement, name="etabs"),
    path('add_subject/', add_subject, name='add_subject'),
    path('add_etab/', add_etablissment, name='add_etablissment'),
    path('add_manager/', add_manager, name='add_manager'),
    path('teachers/add_teacher/', add_teacher, name='add_teacher'),
     path('envoyer_email/', views.message, name='envoyer_email'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_ROOT)