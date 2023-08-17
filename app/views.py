from django.shortcuts import render, HttpResponseRedirect
from .forms import studentregistration
from .models import student

def add_show(request):
    if request.method == 'POST':
        stu = studentregistration(request.POST)
        if stu.is_valid():
            n = stu.cleaned_data['name']
            e = stu.cleaned_data['email']
            pw = stu.cleaned_data['password']
            p = stu.cleaned_data['phone']
            reg = student(name=n, email=e, password=pw, phone=p)
            reg.save()
            stu = studentregistration()
    else:
        stu = studentregistration()
    
    stud = student.objects.all()

    return render(request, 'addandshow.html', {'form': stu, 'dent': stud})
def update(request, id):
    if request.method == 'POST':
        pi = student.objects.get(pk=id)
        fm = studentregistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = student.objects.get(pk=id)
        fm = studentregistration(instance=pi)
    return render(request, 'update.html', {'form': fm})

def destroy(request, id):
    if request.method == 'POST':
        pi = student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
