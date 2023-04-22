
from django.urls import path

from .views import ImageCreateView, IndexView, ImageView, ImageDeleteView, ImageUpdateView, \
    ImageFavoriteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('image/<int:pk>', ImageView.as_view(), name='image_detail'),
    path('images/add/', ImageCreateView.as_view(), name='image_add'),
    path('images/<int:pk>/delete', ImageDeleteView.as_view(), name="image_delete"),
    path('images/<int:pk>/edit', ImageUpdateView.as_view(), name="image_update"),
    path('images/delete/<int:pk>', ImageDeleteView.as_view(), name='image_delete'),
    path('images/<int:pk>/favorite', ImageFavoriteView.as_view(), name='add_favorite')
]
