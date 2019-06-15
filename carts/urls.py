from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.lista_carritos,name='lista_carritos'),
    path('login/',views.login_view, name = 'login'),
    path('logout/',views.logout_view,name='logout'),
    path('registro/',views.registro,name ='registro'),
    path('crear_carritos/',views.crear_carrito, name="crear_carrito")
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)