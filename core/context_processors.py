from django.utils.translation import gettext as _, get_language
from django.conf import settings

def language_context(request):
    current_language = get_language()
    session_language = request.session.get(settings.LANGUAGE_SESSION_KEY)
    
    # Получаем полное название текущего языка
    current_language_name = dict(settings.LANGUAGES).get(current_language, current_language)
    
    # Расширенная отладка
    print(f"=== LANGUAGE DEBUG ===")
    print(f"Current language (get_language()): {current_language}")
    print(f"Session language: {session_language}")
    print(f"Request LANGUAGE_CODE: {getattr(request, 'LANGUAGE_CODE', 'Not set')}")
    print(f"Cookie language: {request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME, 'Not set')}")
    print(f"=== END DEBUG ===")
    
    return {
        'available_languages': settings.LANGUAGES,
        'current_language': current_language,
        'current_language_name': current_language_name,
    }