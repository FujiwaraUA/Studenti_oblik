from django.shortcuts import render
from django.http import HttpResponse


# Views for Groups

def groups_list(request):
    groups = (
        {'id': 1,
         'name': 'Py-11',
         'leader': {'id': 1, 'name': 'Тарас Мельник'}},
        {'id': 2,
         'name': 'Py-12',
         'leader': {'id': 2, 'name': 'Микола Садовський'}},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
