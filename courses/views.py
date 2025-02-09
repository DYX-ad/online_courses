from django.shortcuts import render, redirect, get_object_or_404

from .forms import TopicDocumentForm
from .models import TopicDocument




def index(request):
    return render(request, 'index.html')


def document_list(request):
    if request.method == "POST":
        form = TopicDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = TopicDocumentForm()

    documents = TopicDocument.objects.all()
    return render(request, template_name='document_list.html', context={'form': form, 'documents': documents})


def update_document(request, document_id):
    document = get_object_or_404(TopicDocument, id=document_id)

    if request.method == "POST":
        form = TopicDocumentForm(request.POST, request.FILES, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = TopicDocumentForm(instance=document)

    return render(request, template_name='update_document.html', context={'form': form, 'document': document})


def delete_document(request, document_id):
    document = get_object_or_404(TopicDocument, id=document_id)

    if request.method == 'POST':
        # delete file itself
        if document.file:
            document.file.delete(save=False)

        # delete db row
        document.delete()

    return render(request, template_name='confirm_delete.html', context={'document': document})

   



