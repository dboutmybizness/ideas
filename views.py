from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import get_object_or_404

from ideas.models import *
import ideas.config as CF

def dash(request):
    if not ck_user(request):
        return HttpResponseRedirect(CF.login_page)
    Meta = site_meta(request)

    # ideas = Idea.objects.all()
    recently_viewed = Recently_Viewed.objects.filter(user=request.user).order_by('-viewed_time')[:6]

    t = loader.get_template('ideas/dashboard.html')
    c = RequestContext( request,{
        'Meta' : Meta,
        # 'ideas' : ideas,
        'recently_viewed' : recently_viewed,
    })
    return HttpResponse(t.render(c))

def ideas_main(request):
    if not ck_user(request):
        return HttpResponseRedirect(CF.login_page)
    Meta = site_meta(request)

    ideas = Idea.objects.filter(user=request.user).order_by('name')
    albet = 'abcdefghijklmnopqrstuvwxyz'
    idea_holder = {}
    for letter in albet:
        idea_holder[letter] = []
        for idea in ideas:
            if idea.name.startswith(letter) or idea.name.startswith(letter.capitalize()):

                idea_holder[letter].append(idea)



    t = loader.get_template('ideas/ideas.html')
    c = RequestContext( request,{
        'Meta' : Meta,
        'idea_holder' : idea_holder,
        'albet' : albet,
    })
    return HttpResponse(t.render(c))

def idea_landing(request, id):
    if not ck_user(request):
        return HttpResponseRedirect(CF.login_page)
    Meta = site_meta(request)
    
    idea = get_object_or_404(Idea, pk = id, user=request.user)
    from datetime import datetime

    ck_rv = Recently_Viewed.objects.filter(user=request.user,idea=idea).delete()
    # if ck_rv:
    #     for rec in ck_rv:
    #         rec.delete()

    rv = Recently_Viewed(
        idea=idea,
        user=request.user,
        viewed_time = datetime.now()
    )
    rv.save()

    if request.method == 'POST':
        if 'note' in request.POST:
            if request.POST['note']:
                #save it
                note = Note(
                    idea = idea,
                    txt = request.POST['note']
                )
                note.save()
        if 'form-note-create' in request.POST:
            n = Note(idea=idea)
            return save_note(n, request.POST)

    
    

    t = loader.get_template('ideas/landing.html')
    c = RequestContext( request,{
        'Meta' : Meta,
        'idea' : idea,
    })
    return HttpResponse(t.render(c))

def idea_create(request):
    if not ck_user(request):
        return HttpResponseRedirect(CF.login_page)
    Meta = site_meta(request)

    itypes = Idea_Type.objects.all().order_by('idea_type')

    t = loader.get_template('ideas/ideas.html')
    c = RequestContext( request,{
        'Meta' : Meta,
        'itypes' : itypes,
    })
    return HttpResponse(t.render(c))

def save_note(note, post):
    import json

    response_data = {
        'result' : 0,
    }

    pars = post
    note.txt = pars['txt']
    note.headline = pars['headline']
    note.save()

    if 'form-note-create' in post:
        response_data['datetime'] = str(note.created_time)
        response_data['link'] = note.link()

    response_data['result'] = 1

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def note_landing(request, idea_id, note_id):
    if not ck_user(request):
        return HttpResponseRedirect(CF.login_page)
    Meta = site_meta(request)

    note = get_object_or_404(Note, pk = note_id, idea=idea_id, idea__user=request.user)

    if request.method == 'POST' and 'form-note-save' in request.POST:
        return save_note(note, request.POST)


    t = loader.get_template('ideas/note_landing.html')
    c = RequestContext( request,{
        'Meta' : Meta,
        'note' : note,
    })
    return HttpResponse(t.render(c))

def site_meta(request):
    CF.current_path = request.get_full_path()
    return CF

def ck_user(request):
    if request.user.is_authenticated():
        return True
    return False