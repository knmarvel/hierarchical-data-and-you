from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from filecabinet.models import File
from filecabinet.forms import LoginForm, FileForm

# Create your views here.

def index(request):
    html = 'index.html'
    data = File.objects.all()
    return render(request, html, {'data': data})


@login_required
def add_file(request):
    html = "generic_form.html"
    user = request.user
    if request.method =="POST":
        form = FileForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_file = File.objects.create(
                name=data['name'],
                parent=data['parent'],
            )
            return HttpResponseRedirect(
                request.GET.get('next', reverse('homepage'))
            )
    form = FileForm()
    return render(request, html, {'form': form})


def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username = data['username'], password = data['password']
                )
            if user:
                login(request, user)
                
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'generic_form.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request, "generic_form.html", {"form": form})

    form = UserCreationForm()
    return render(request = request,
                  template_name = "generic_form.html",
                  context={"form":form})

