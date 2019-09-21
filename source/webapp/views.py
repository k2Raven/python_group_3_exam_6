from django.shortcuts import render
from webapp.models import Record


def index_view(request, *args, **kwargs):
    records = Record.objects.order_by('-created_at').filter(status='active')
    return render(request, 'index.html', context={
        'records': records
    })