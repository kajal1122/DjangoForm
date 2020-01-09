from django.shortcuts import render,redirect
from django.template import loader
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import QuestionSet
from .forms import QuestionForm
# Create your views here.

def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            post = form.save()

            context = {}
            template = loader.get_template('thankyou.html')
            return HttpResponse(template.render(context,request))
    else:
        form = QuestionForm()

    return render(request,
                  'create.html',
                  {
                      'form': form
                  })
