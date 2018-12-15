from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'surveys/index.html')

def process(request):
    print(request.POST)
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']

    content = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language']
    }
    return redirect('/result', content)

def result(request):

    return render(request, 'surveys/result.html')
