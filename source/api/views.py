from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet

from api.serializers import ImageSerializer
from gallery.models import Image


class ImageView(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def add_image_to_favorite(self, request, *args, **kwargs):
        image = self.get_object()
        user = request.user
        user.favorites.add(image)
        return JsonResponse({'result': 'Image successfully added to favorites'})

    def image_remove_from_favorite(self, request, *args, **kwargs):
        image = self.get_object()
        user = request.user
        user.favorites.remove(image)
        return JsonResponse({'result': 'Image successfully removed from favorites'})
