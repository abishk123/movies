from django.shortcuts import render
from django.http import HttpResponse

def movies_seen(request):
    return HttpResponse('''
    <h1>12th FAIL</h1>
    <h1>JAB WE MET</h1>
    <h1>ZINDAGI NA MILEGA DUBARA</h1>
    ''')

def upcoming_movies(request):
    return HttpResponse('''
<h1>NARENDRA MODI<h1>
<h1>PUSHPA 2</h2>''')
