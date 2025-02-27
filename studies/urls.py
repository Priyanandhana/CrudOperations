from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_list, name='study_list'),
    path('add/', views.study_add, name='study_add'),
    path('view/<int:id>/', views.study_view, name='study_view'),
    path('edit/<int:id>/', views.study_edit, name='study_edit'),
    path('delete/<int:study_id>/', views.study_delete, name='study_delete'),
    path('delete_bulk/', views.study_delete_bulk, name='study_delete_bulk'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)