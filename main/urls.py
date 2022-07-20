from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.base),
    path('chest/', views.chest),
    path('shoulders/', views.shoulders),
    path('triceps/', views.triceps),
    path('back/', views.back),
    path('biceps/', views.biceps),
    path('legs/', views.legs),
    path('about/', views.about),
    path('gurate/', views.gurate),
    path('pick/', views.pick, name='pick'),
    path('display/', views.display),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
