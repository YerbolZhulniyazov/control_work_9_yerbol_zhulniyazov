from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from gallery.forms import ImageForm
from gallery.models import Image


class IndexView(ListView):
    template_name = 'index.html'
    model = Image
    context_object_name = 'images'
    ordering = '-created_at'


class ImageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'add_image.html'
    form_class = ImageForm
    model = Image

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.request.user.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ImageView(DetailView):
    template_name = 'image_detail.html'
    model = Image

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        image = self.object
        users = image.users.all
        context['users'] = users
        return context


class ImageUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'update_image.html'
    form_class = ImageForm
    model = Image
    context_object_name = 'image'
    permission_required = 'gallery.change_image'

    def get_success_url(self):
        return reverse('image_detail', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


class ImageDeleteView(PermissionRequiredMixin, DeleteView):
    model = Image
    success_url = reverse_lazy('index')

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user


class ImageFavoriteView(View):
    def post(self, request, *args, **kwargs):
        image = get_object_or_404(Image, pk=kwargs.get('pk'))
        user = request.user
        if image in user.favorites.all():
            user.favorites.remove(image)
            return redirect('index')
        user.favorites.add(image)
        return redirect('index')
