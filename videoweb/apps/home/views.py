from django.shortcuts import render_to_response
from django.template import RequestContext
from videoweb.apps.home.forms import *
from videoweb.apps.appvideos.models import uploadvideo
from .forms import UploadVideoForm, NewAccountForm
from videoweb.apps.conversion.tasks import *

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

import time

## Manejo de la vista inicio
def index_view(request):
    uploadvideo1 = uploadvideo.objects.order_by('-date').filter(status=True)
    ctx = {'uploadvideo': uploadvideo1}
    return render_to_response('home/index.html', ctx, context_instance=RequestContext(request))

## Manejo de la vista para creacion de cuenta
def newaccount_view(request):
    if request.method == 'POST':
        form = NewAccountForm(request.POST)
        info = "Inicializando"
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            n = User()
            n.first_name = first_name;
            n.last_name = last_name;
            n.email = email;
            n.username = username;
            n.set_password(password);
            n.save();
            info = "new account :)"
            form = NewAccountForm()
            ctx = {'form': form, 'info': info}
            return render_to_response('home/newaccount.html', ctx, context_instance=RequestContext(request))
        else:
            info = ":( no save... grown data"
            form = NewAccountForm()
            ctx = {'form': form, 'info': info}
            return render_to_response('home/newaccount.html', ctx, context_instance=RequestContext(request))
    else:
        form = NewAccountForm()
        ctx = {'form': form}
        return render_to_response('home/newaccount.html', ctx, context_instance=RequestContext(request))

## Manejo de la vista que le muestra un video a un usuario
def myvideos_view(request):
    uploadvideo1 = uploadvideo.objects.order_by('-date').filter(user_id=request.user.id, status=True)
    ctx = {'uploadvideo':uploadvideo1}
    return render_to_response('home/myvideos.html',ctx,context_instance=RequestContext(request))
    #return render_to_response('home/index.html', context_instance=RequestContext(request))


## Vista about
def about_view(request):
    uploadvideo1 = uploadvideo.objects.filter(status=True)
    ctx = {'uploadvideo':uploadvideo1}
    return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))


## Manejo de la vista para autenticarse en el sistema

def login_view(request):
    mensaje=""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                usuario=authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(request, usuario)
                    return HttpResponseRedirect('/')
                else:
                    mensaje = "usuario y/o password incorrecto"
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje}
        return render_to_response('home/login.html', ctx, context_instance=RequestContext(request))

## Manejo de la vista para salir del sistema
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


## Manejo de la vista para subir el video
def uploadvideo_view(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = 	UploadVideoForm(request.POST, request.FILES)
            info =	"Inicializando"
            if form.is_valid():
                name 	=	form.cleaned_data['name']
                name = str(name.replace(" ","_"))
                video 	=	form.cleaned_data['video']
                #date	=	form.cleaned_data['date']
                message	= 	form.cleaned_data['message']
                #datepublish = form.cleaned_data['datepublish']
                date=str(time.strftime('%Y-%m-%d %H:%M:%S'))
                #name=str(name.replace(" ",""))
                user = User.objects.get(id= request.user.id);
                v 	=	uploadvideo();
                v.name 	= name;
                v.video = video;
                v.date  = date;
                v.status = False;
                v.message = message;
                v.datepublish = date;
                v.user = user;
                v.save();
                result = convertir.delay(str(os.path.basename(video.name).replace(" ","_")) , name)
                info = "Proccesing your video ...."
                form = UploadVideoForm()
                ctx = {'form':form, 'info':info}
                return render_to_response('home/upload.html',ctx, context_instance=RequestContext(request))
            else:
                info = ":( no save... grown data"
            form = UploadVideoForm()
            ctx = {'form':form, 'info':info}
            return render_to_response('home/upload.html', ctx, context_instance=RequestContext(request))
        else:
            form=UploadVideoForm()
            ctx = {'form':form}
            return render_to_response('home/upload.html', ctx, context_instance=RequestContext(request))
    else:
        message = "user most login"
        ctx = {'msg':message}
        return render_to_response('home/index.html', ctx,context_instance=RequestContext(request))

