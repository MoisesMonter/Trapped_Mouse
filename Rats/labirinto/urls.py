from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #path('',views.Home,name='home'),
    path('',views.labirinto,name='labirinto'),
    path('labirinto',views.labirinto,name='labirinto'),
    path('labirinto2',views.labirinto2,name='labirinto2'),
]
if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)