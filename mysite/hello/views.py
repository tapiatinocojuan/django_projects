from django.http import HttpResponse

def sessfun(request) :
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    oldval = request.COOKIES.get('dj4e_cookie', None)
    if oldval is None:
        resp.set_cookie('dj4e_cookie', 'fdad122d', max_age=1000)

    return resp