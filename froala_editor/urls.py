from django.urls import path

from froala_editor import views

urlpatterns = [
    path('upload/image/', views.image_upload, name='froala_editor_image_upload'),
    path('upload/file/', views.file_upload, name='froala_editor_file_upload'),
]
