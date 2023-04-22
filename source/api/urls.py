from django.urls import path, include
from rest_framework import routers
from api.views import ImageView

router = routers.DefaultRouter()
router.register('images', ImageView)
urlpatterns = [
    path('', include(router.urls)),
    path('image/<int:pk>', ImageView.as_view({'get': 'add_image_to_favorite'}), name='fav'),
    path('image/<int:pk>', ImageView.as_view({'get': 'image_remove_favorite'}), name='fromfav'),
]
