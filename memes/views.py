from django.core.paginator import Paginator
from django.shortcuts import render

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
