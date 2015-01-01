from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout

from ideas.models import *

def main(request):
    if not ck_user(request):
        return HttpResponseRedirect('/login.html')
    Meta = site_meta(request)

    ideas = Idea.objects.all()

    t = loader.get_template('ideas/dashboard.html')
    c = RequestContext( request,{
        'Meta' : Meta,
        'ideas' : ideas,
    })
    return HttpResponse(t.render(c))

def idea_landing(request, id):
    if not ck_user(request):
        return HttpResponseRedirect('/login.html')
    Meta = site_meta(request)


    from django.shortcuts import get_object_or_404
    
    idea = get_object_or_404(Idea, pk = id)

    if request.method == 'POST':
        if 'note' in request.POST:
            if request.POST['note']:
                #save it
                note = Note(
                    idea = idea,
                    txt = request.POST['note']
                )
                note.save()

    
    

    t = loader.get_template('ideas/landing.html')
    c = RequestContext( request,{
        'Meta' : Meta,
        'idea' : idea,
    })
    return HttpResponse(t.render(c))

def idea_create(request):
    if not ck_user(request):
        return HttpResponseRedirect('/login.html')
    Meta = site_meta(request)

    itypes = Idea_Type.objects.all().order_by('idea_type')

    t = loader.get_template('ideas/create.html')
    c = RequestContext( request,{
        'Meta' : Meta,
        'itypes' : itypes,
    })
    return HttpResponse(t.render(c))

def site_meta(request):
    return 1

def ck_user(request):
    return 1