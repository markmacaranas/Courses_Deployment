from django.shortcuts import render, redirect
from .models import Course, Description, Comment

# Create your views here.
def index(request):
    context = {
    'courses': Course.objects.all(),
    'descriptions': Description.objects.all()
    }
    print "*"*100
    print context
    print "*"*100
    return render(request, 'courses/index.html', context)

def addNew(request):
    if request.method == "POST":
        newcourse = Course.objects.create(name=request.POST['name'])
        des_id = Course.objects.get(id=newcourse.id)
        Description.objects.create(course=des_id, description=request.POST['description'])
    return redirect('/')

def remove(request, id):
    if request.method == 'POST':
        if request.POST['submit'] == 'YES':
            coursekey = Course.objects.get(id=id).delete()
            return redirect('/')
        elif request.POST['submit'] == 'NO':
            return redirect('/')
    else:
        course = Course.objects.get(id=id)
        context = {'course': course}
        return render(request, 'courses/remove.html', context)
