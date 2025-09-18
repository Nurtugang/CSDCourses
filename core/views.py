from django.conf import settings
from django.utils import translation
from django.shortcuts import render, redirect
from django.urls import translate_url
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.translation import get_language, gettext as _
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    return render(request, 'courses.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')


def change_language(request, language_code):
    # Проверяем, что язык поддерживается
    if language_code in [lang[0] for lang in settings.LANGUAGES]:
        # Сохраняем в сессии
        request.session['django_language'] = language_code
        
        # Получаем URL для редиректа
        redirect_to = request.META.get('HTTP_REFERER', '/')
        return HttpResponseRedirect(redirect_to)
    
    # Если язык не поддерживается, редирект на главную
    return redirect('index')

def test_language(request):
    current_lang = get_language()
    session_lang = request.session.get('django_language', 'Not set')
    
    test_translation = _("Computer Science Courses")
    
    html = f"""
    <h1>Language Test</h1>
    <p>Current Language: {current_lang}</p>
    <p>Session Language: {session_lang}</p>
    <p>Test Translation: {test_translation}</p>
    <p>Available Languages: {dict(settings.LANGUAGES)}</p>
    
    <h2>Change Language:</h2>
    <a href="/change-language/en/">English</a> | 
    <a href="/change-language/ru/">Russian</a> | 
    <a href="/change-language/kk/">Kazakh</a>
    
    <br><br>
    <a href="/">Back to Home</a>
    """
    
    return HttpResponse(html)