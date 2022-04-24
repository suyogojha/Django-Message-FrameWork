from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages

# Create your views here.
def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            #adding message to the user
            messages.add_message(request, messages.SUCCESS, 'Registration Successful') 
            #adding more message
            messages.info(request, 'Please login to continue')
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userreg.html', {'form': fm})
