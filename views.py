from django.shortcuts import render

def index(request):
    return render(request, 'personal/home.html', {'title':['Home']})

def blog(request):
    return render(request, 'personal/blog.html', {'title':['Blog']})

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me, please email me', 'info@imamshafai.online']})
