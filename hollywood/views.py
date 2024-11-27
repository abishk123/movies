from django.shortcuts import render
from django.http import HttpResponse

def movies_seen(request):
    return HttpResponse('''
    <h1>PERSUITS OF HAPPINESS</h1>
    <h1>CREED</h1>
    <h1>EVIL DEAD RISE</h1>
    ''')

def upcoming_movies(request):
    return HttpResponse('''
<h1>DANGER<h1>
<h1>CREED IV</h2>''')
