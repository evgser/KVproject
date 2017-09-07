from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import Http404
from . import models
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth.models import User

def main(request):
    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    return render(request, 'landing/main.html', args)

