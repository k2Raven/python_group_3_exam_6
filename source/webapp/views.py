from django.shortcuts import render, redirect, get_object_or_404

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


def record_update_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'GET':
        form = RecordForm(data={
            'author': record.author,
            'email_author': record.email_author,
            'text': record.text
        })
        return render(request, 'update_render.html', context={'form': form, 'record': record})
    elif request.method == 'POST':
        form = RecordForm(data=request.POST)
        if form.is_valid():
            record.author = form.cleaned_data['author']
            record.email_author = form.cleaned_data['email_author']
            record.text = form.cleaned_data['text']
            record.save()
            return redirect('/')
        else:
            return render(request, 'update_render.html', context={'form': form, 'record': record})


def record_delete_view(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete_record.html', context={'record': record})
    elif request.method == 'POST':
        record.delete()
        return redirect('index')