from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,"index.html")
# Create your views here.

def login_action(request):

    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)

        if user is not None:

            auth.login(request,user)
            #response.set_cookie('user',uname,3600)
            request.session['user']=username
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html',{'error':'username or password is wrong'})

@login_required
def event_manage(request):
    event_list = Event.objects.all()
    #uuname = request.COOKIES.get('user','')
    uuname = request.session.get('user','')
    return render(request,'event_manage.html',{"user":uuname,"events":event_list})


@login_required
def guest_manage(request):
    guest_list = Guest.objects.all()
    #uuname = request.COOKIES.get('user','')
    uuname = request.session.get('user','')
    paginator = Paginator(guest_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts =paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'guest_manage.html', {"user":uuname, "guests":contacts})

@login_required
def search_name(request):
    #uuname = request.COOKIES.get('user','')
    uuname = request.session.get('user','')
    search_name = request.GET.get("name","")
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,'event_manage.html',{"user":uuname,"events":event_list})

@login_required
def sign_index(request,eid):
    event = get_object_or_404(Event,id = eid)
    return render(request,'sign_index.html',{"event":event})

@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response


@login_required
def sign_index_action(request,eid):
    event = get_object_or_404(Event,id = eid)
    phone = request.POST.get('phone','')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html',
                      {'event': event, 'hint': 'phone error.'})

    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign_index.html',
                      {'event': event, 'hint': 'event id or phone error.'})

    result = Guest.objects.get(event_id=eid, phone=phone)

    if result.sign:
        return render(request, 'sign_index.html',
                      {'event': event, 'hint': "user has sign in."})
    else:
        Guest.objects.filter(event_id=eid, phone=phone).update(sign='1')
        return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in success!',
                                                   'user': result,
                                                   'guest': result
                                                   })
