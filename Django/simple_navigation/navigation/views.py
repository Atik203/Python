from django.shortcuts import render
import datetime

# Create your views here.
def about(request):
    return render(request, 'navigation/about.html')
def contact(request):
    d = {'email': 'test@email.com','birthday':datetime.datetime.now(), 'phone': '123-456-7890','list': [1,2,3],'age': 20, 'name': 'John','courses': [
        {
        'id': 1,
        'name': 'Math',
    },
        {
        'id': 2,
        'name': 'Science',
    
    },
        {
        'id': 3,
        'name': 'English',}],'list2':['python','java','c++']}
    return render(request, 'navigation/contact.html', d)