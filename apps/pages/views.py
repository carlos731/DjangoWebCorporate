from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    # messages.debug(request, 'SQL statements were executed.')
    # messages.info(request, 'Theree credits remain in your account.')    
    # messages.success(request, 'Profile details updated.')
    # messages.warning(request, 'Your account expires in three days.')
    # messages.error(request, 'Document deleted.')
    
    return render(request, 'index.html')