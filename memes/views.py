from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from memes.forms import MemForm
from memes.mixins import ListObjectsMixin
from memes.models import Mem, Movie


class ListMems(ListObjectsMixin, View):
    model = Mem
    template_name = 'memes/index.html'
    template_include = 'memes/include/mems.html'


class ListMovies(ListObjectsMixin, View):
    model = Movie
    template_name = 'memes/movies.html'
    template_include = 'memes/include/movies.html'


class ViewMem(View):
    def get(self, request, slug):
        mem = get_object_or_404(Mem, slug=slug)

        return render(
            request,
            'memes/mem.html',
            context={
                'mem': mem
            }
        )


class CreateMem(View):
    def get(self, request):
        form = MemForm()

        return render(
            request,
            'memes/create_mem.html',
            context={
                'form': form
            }
        )

    def post(self, request):
        form = MemForm(request.POST, request.FILES)

        if form.is_valid():
            mem = form.save()
            mem.save()

            return redirect(mem)

        return render(
            request,
            'memes/create_mem.html',
            context={
                'form': form
            }
        )
