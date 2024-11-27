from django.shortcuts import render
from django.http import HttpResponse

def t_movies_seen(request):
    return HttpResponse('''
    <h1>BAHUBALI</h1>
    <h1>KANGUVA</h1>
    <h1>MECHANIC ROCKEY</h1>
    <h1>ARJUN REDDY</h1>
    <h1>RRR</h1>
    <h1>DEVARA</h1>
    ''')

def t_upcoming_movies(request):
    return HttpResponse('''
<h1>SPIRIT<h1>
<h1>SALAAR-2</h1>
<h1>GAME CHANGER<h1>
<h1>KALKI-2</h1>
<h1>RAJASAAB</h1>''')
def t_best_movies(request):
    return HttpResponse('<h1>TUMBBAD<h1>')

