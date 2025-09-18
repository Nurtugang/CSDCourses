from django.utils import translation
from django.conf import settings

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = self.get_language_from_request(request)
        
        # Принудительно активируем язык
        translation.activate(language)
        request.LANGUAGE_CODE = language
        
        response = self.get_response(request)
        
        # Деактивируем язык после обработки запроса
        translation.deactivate()
        
        return response
    
    def get_language_from_request(self, request):
        """
        Определяем язык в следующем порядке:
        1. Из сессии
        2. Из cookie
        3. Из Accept-Language заголовка
        4. По умолчанию
        """
        supported_languages = [lang[0] for lang in settings.LANGUAGES]
        
        # 1. Проверяем сессию
        if hasattr(request, 'session'):
            session_language = request.session.get(settings.LANGUAGE_SESSION_KEY)
            if session_language and session_language in supported_languages:
                print(f"Using language from session: {session_language}")
                return session_language
        
        # 2. Проверяем cookie
        cookie_language = request.COOKIES.get(settings.LANGUAGE_COOKIE_NAME)
        if cookie_language and cookie_language in supported_languages:
            print(f"Using language from cookie: {cookie_language}")
            return cookie_language
        
        # 3. Проверяем Accept-Language заголовок
        accept_language = request.META.get('HTTP_ACCEPT_LANGUAGE', '')
        for lang_code in supported_languages:
            if lang_code in accept_language:
                print(f"Using language from Accept-Language: {lang_code}")
                return lang_code
        
        # 4. По умолчанию
        print(f"Using default language: {settings.LANGUAGE_CODE}")
        return settings.LANGUAGE_CODE