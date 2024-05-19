from django.contrib.auth import login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from requests import Response

from social_django.utils import psa


@csrf_exempt
@psa('social:complete')
def google_login(request, backend):
    token = request.POST.get('token')
    user = request.backend.do_auth(token)

    if user:
        login(request, user)
        return Response('Logged in')
    else:
        return Response('Error logging in')
