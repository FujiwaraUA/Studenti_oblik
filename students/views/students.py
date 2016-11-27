from django.shortcuts import render
from django.http import HttpResponse


# Views for Students

def students_list(request):
    students = (
        {'id': 1,
         'first_name': 'Віталій',
         'last_name': 'Кононенко',
         'ticket': 235,
         'image': 'img/me1.jpg'},
        {'id': 2,
         'first_name': 'Андрій',
         'last_name': 'Іваненко',
         'ticket': 2123,
         'image': 'img/me.jpeg'},
        {'id': 3,
         'first_name': 'Василь',
         'last_name': 'Шевчено',
         'ticket': 21,
         'image': 'img/piv.png'},
    )
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Student Add Form</h1>')


def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student {}</h1>'.format(sid))


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)

