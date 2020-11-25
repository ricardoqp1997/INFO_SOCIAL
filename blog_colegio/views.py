from django.shortcuts import render
from django.contrib.auth.models import Group

from .models import BlogColegio

from django.views.generic import (
    ListView,
    DetailView,
)


class BlogList(ListView):

    paginate_by = 5
    queryset = BlogColegio.objects.all()
    template_name = 'blog.html'

    def get_context_data(self, *, object_list=None, **kwargs):

        tipo_usuario = Group.objects.get(user=self.request.user).name

        context = super(BlogList, self).get_context_data(**kwargs)

        context.update(
            {
                'Title': 'Noticias institucionales',
                'tipo_usuario': tipo_usuario,
            }
        )

        return context


class BlogDetail(DetailView):

    queryset = BlogColegio.objects.all()
    template_name = 'blog_detalles.html'
