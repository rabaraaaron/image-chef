from django.urls import path

from api.image_chef_api import views

urlpatterns = [
    path('health/', views.health, name='health'),
    path('text-to-image/', views.text_to_image, name='text-to-image'),
    path('text-guided-image-to-image/', views.text_guided_image_to_image,
         name='text-guided-image-to-image'),
    path('image-inpainting/', views.image_inpainting,
         name='image-inpainting'),
    path('improve-image-quality/', views.improve_image_quality,
         name='improve-image-quality')
]
