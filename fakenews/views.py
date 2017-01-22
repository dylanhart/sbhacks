from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, reverse

import json
from hashlib import md5

# Create your views here.

def index(req):
    return render(req, 'fakenews/index.html')

@require_http_methods(['POST'])
def detect(req):
    hasher = md5()
    url = req.POST.get('url', None)
    if not url:
        res = {'success': False, 'msg': 'url is required'}
        return HttpResponse(json.dumps(res), content_type='application/json')

    hasher.update(url.encode('utf-8'))
    url_hash = hasher.hexdigest()
    res = {
        'success': True,
        'results': reverse('fn:results', kwargs={'url_hash': url_hash}),
    }

    return HttpResponse(json.dumps(res), content_type='application/json')

def results(req, url_hash):
    return HttpResponse('not implemented')
