from django.shortcuts import render

# Create your views here.

def cat_list(request):
    return render(request, 'feed/cat_list.html')
