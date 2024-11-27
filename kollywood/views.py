from django.shortcuts import render
from django.http import HttpResponse

def k_movies_seen(request):
    return HttpResponse('''
    <h1>BHEEMA</h1>
    <h1>NAVAGRAHA</h1>
    <h1>OM</h1>
    ''')

def k_upcoming_movies(request):
    return HttpResponse('''
<h1>UI<h1>
<h1>KGF-3</h2>''')

