from django.shortcuts import render, redirect

from webapp.forms import RecordForm
from webapp.models import Record


def index_view(request, *args, **kwargs):
    records = Record.objects.order_by('-created_at').filter(status='active')
    return render(request, 'index.html', context={
        'records': records
    })


def record_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = RecordForm()
        return render(request, 'new_record.html', context={'form': form})
    elif request.method == 'POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():
            Record.objects.create(
                email_author=form.cleaned_data['email_author'],
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text']
            )
            return redirect('/')

        else:
            return render(request, 'new_record.html', context={'form': form})
