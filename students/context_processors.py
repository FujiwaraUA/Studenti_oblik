from Studenti_oblik.settings import PORTAL_URL

def students_proc(request):
    return {'PORTAL_URL': PORTAL_URL}