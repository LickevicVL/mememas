from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from memes.forms import MemForm
from memes.models import Mem


def index(request):
    mems = Mem.objects.all().order_by('-created_at')

    paginator = Paginator(mems, 6)
    page = int(request.GET.get('page', 1))

    if page > 1:
        return render(
            request,
            'memes/includes/mems.html',
            {'mems': paginator.get_page(page)}
        )

    return render(
        request,
        'memes/index.html',
        context={
            'mems': paginator.get_page(page),
            'pages': paginator.num_pages
        }
    )


def view_mem(request, slug):
    mem = get_object_or_404(Mem, slug=slug)

    return render(
        request,
        'memes/mem.html',
        context={
            'mem': mem
        }
    )


def create_mem(request):
    if request.method == 'POST':
        print('files', request.FILES)
        form = MemForm(request.POST, request.FILES)

        if form.is_valid():
            mem = form.save()
            mem.save()

            return redirect(mem)
    else:
        form = MemForm()

    return render(
        request,
        'memes/create_mem.html',
        context={
            'form': form
        }
    )
