from django.shortcuts import render

from . import forms


# Create your views here.
def about(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        return render(request, 'app/about.html', {'name': name, 'email': email})
    else:
        return render(request, 'app/about.html')    

def form(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     return render(request, 'app/form.html', {'name': name, 'email': email})
    # else:
    return render(request, 'app/form.html')

def form2(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')
        select = request.GET.get('select')
        return render(request, 'app/form2.html', {'name': name, 'email': email , 'select': select})
    return render(request, 'app/form2.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = forms.contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./app/upload/'+file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            # image = form.cleaned_data['image']
            # with open('./app/upload/'+image.name, 'wb+') as destination:
            #     for chunk in image.chunks():
            #         destination.write(chunk)
            
            print(form.cleaned_data)
        return render(request, 'app/DjangoForm.html', {'form': form})
    else:
        form = forms.contactForm()
    return render(request, 'app/DjangoForm.html', {'form': form})

def StudentForm(request):
    if request.method == 'POST':
        form = forms.StudentData(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'app/DjangoForm.html', {'form': form})
    else:
        form = forms.StudentData()
    return render(request, 'app/DjangoForm.html', {'form': form})


def PasswordForm(request):
    if request.method == 'POST':
        form = forms.PasswordValidation(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'app/DjangoForm.html', {'form': form})
    else:
        form = forms.PasswordValidation()
    return render(request, 'app/DjangoForm.html', {'form': form})