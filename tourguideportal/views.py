from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tourguideportal.forms import SignUpForm
from django.http import HttpResponseRedirect
# Create your views here.
def indexview(request):
    return render(request,'tourguideportal/index.html')
@login_required
def delhiview(request):
    return render(request,'tourguideportal/delhi.html')
@login_required
def vizagview(request):
    return render(request,'tourguideportal/vizag.html')
@login_required
def hyderabadview(request):
    return render(request,'tourguideportal/hyderabad.html')
@login_required
def goaview(request):
    return render(request,'tourguideportal/goa.html')
@login_required
def kolkataview(request):
    return render(request,'tourguideportal/kolkata.html')
@login_required
def chennaiview(request):
    return render(request,'tourguideportal/chennai.html')
@login_required
def bangaloreview(request):
    return render(request,'tourguideportal/bangalore.html')

@login_required
def mumbaiview(request):
    return render(request,'tourguideportal/mumbai.html')

@login_required
def aboutview(request):
    return render(request,'tourguideportal/about.html')

@login_required
def contactview(request):
    return render(request,'tourguideportal/contact.html')

@login_required
def beachroadview(request):
    return render(request,'tourguideportal/beachroad.html')
@login_required
def moreplacesview(request):
    return render(request,'tourguideportal/moreplaces.html')
@login_required
def kailasagiriview(request):
    return render(request,'tourguideportal/kailasagiri.html')
@login_required
def arakuview(request):
    return render(request,'tourguideportal/araku.html')
@login_required
def rushikondaview(request):
    return render(request,'tourguideportal/rushikonda.html')
@login_required
def harbourview(request):
    return render(request,'tourguideportal/harbour.html')
@login_required
def vparksview(request):
    return render(request,'tourguideportal/vparks.html')
@login_required
def vhotelsview(request):
    return render(request,'tourguideportal/vhotels.html')

def logout_view(request):
    return render(request,'tourguideportal/logout.html')

def signup_view(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        # if form.is_valid():
        #     form.save()
        user=form.save()
        user.set_password(user.password)
        user.save()
        # # form.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'tourguideportal/signup.html',{'form':form})















