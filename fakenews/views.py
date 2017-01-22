from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, reverse, get_object_or_404

import json
import random
import logging
from hashlib import md5

from FakeNewsDetector import spoof_proof

from . import forms, models

logger = logging.getLogger(__name__)

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

    try:
        out = spoof_proof.run(url) == 1
    except Exception as e:
        logger.error('failed to spoof_proof')
        logger.error(str(e))
        res = {'success': False, 'msg': 'An error occurred while processing this site.'}
        return HttpResponse(json.dumps(res), content_type='application/json')

    hasher.update(url.encode('utf-8'))
    url_hash = hasher.hexdigest()

    models.Result.objects.create(
        url_hash=url_hash,
        is_real=out,
    )

    res = {
        'success': True,
        'results': reverse('fn:results', kwargs={'url_hash': url_hash}),
    }

    return HttpResponse(json.dumps(res), content_type='application/json')


def results(req, url_hash):
    result = get_object_or_404(models.Result, url_hash=url_hash)
    return render(req, 'fakenews/results.html', {
        'overall': result.is_real,
        'breakdown': {
            'Tone Analysis': result.is_real,
        }
    })
