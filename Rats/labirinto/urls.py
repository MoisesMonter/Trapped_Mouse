from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    #path('',views.Home,name='home'),
    path('',views.labirinto,name='labirinto'),
    path('labirinto',views.labirinto,name='labirinto'),
    path('labirinto=?2',views.labirinto2,name='labirinto2'),
    path('labirinto=?3',views.labirinto3,name='labirinto3'),
    path('labirinto=?4',views.labirinto4,name='labirinto4'),
]
if settings.DEBUG:     
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)