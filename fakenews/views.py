from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, reverse

import json
import random
from hashlib import md5

from . import forms

# Create your views here.

def index(req):
    return render(req, 'fakenews/index.html')

@require_http_methods(['POST'])
def detect(req):
    hasher = md5()

    form = forms.DetectForm(data=req.POST)
    if not form.is_valid():
        msg = []
        for field, errors in form.errors.items():
            for error in errors:
                msg.append('{}: {}'.format(field, error))
        res = {'success': False, 'msg': ', '.join(msg)}
        return HttpResponse(json.dumps(res), content_type='application/json')

    url = form.cleaned_data['url']

    hasher.update(url.encode('utf-8'))
    url_hash = hasher.hexdigest()
    res = {
        'success': True,
        'results': reverse('fn:results', kwargs={'url_hash': url_hash}),
    }

    return HttpResponse(json.dumps(res), content_type='application/json')

def results(req, url_hash):
    passes = bool(random.getrandbits(1))
    return render(req, 'fakenews/results.html', {
        'overall': passes,
        'breakdown': {
            'Tone Analysis': passes,
        }
    })
