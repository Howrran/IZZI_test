# from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from user.forms.add_users_form import DocumentForm

def add_users(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            # newdoc = Document(docfile = request.FILES['docfile'])
            # newdoc.save()

            # Redirect to the document list after POST
            # return HttpResponseRedirect(reverse('myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    # documents = Document.objects.all()

    # Render list page with the documents and the form
    # return render_to_response(
    #     'myapp/list.html',
    #     {'documents': documents, 'form': form},
    #     context_instance=RequestContext(request)
    # )