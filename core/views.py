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




def course_detail(request, course_slug):
    # Тестовые данные для разных курсов
    course_data = {
        'web-design': {
            'title': 'Web Design & Development Course',
            'description': 'Complete course for learning web design and development from scratch. Master HTML, CSS, JavaScript, and modern frameworks to build stunning websites.',
            'price': '$149.00',
            'rating': 4.8,
            'students': 1250,
            'duration': '12 weeks',
            'instructor': 'John Doe',
            'instructor_bio': 'Senior Full-Stack Developer with 8+ years of experience',
            'total_lessons': 45,
            'total_hours': 35,
            'level': 'All Levels',
            'language': 'English',
            'certificate': True,
            'lifetime_access': True
        },
        'python-programming': {
            'title': 'Python Programming Complete Course',
            'description': 'Learn Python programming from basics to advanced concepts. Build real-world projects and master data science, web development, and automation.',
            'price': '$199.00',
            'rating': 4.9,
            'students': 2100,
            'duration': '16 weeks',
            'instructor': 'Jane Smith',
            'instructor_bio': 'Data Scientist and Python Expert with 10+ years experience',
            'total_lessons': 60,
            'total_hours': 48,
            'level': 'Beginner to Advanced',
            'language': 'English',
            'certificate': True,
            'lifetime_access': True
        },
        'data-science': {
            'title': 'Data Science & Machine Learning Bootcamp',
            'description': 'Master data science and machine learning with Python. Learn statistics, data visualization, and build ML models for real business problems.',
            'price': '$299.00',
            'rating': 4.7,
            'students': 890,
            'duration': '20 weeks',
            'instructor': 'Dr. Michael Chen',
            'instructor_bio': 'PhD in Computer Science, ML Research Scientist at Google',
            'total_lessons': 75,
            'total_hours': 65,
            'level': 'Intermediate to Advanced',
            'language': 'English',
            'certificate': True,
            'lifetime_access': True
        },
        'mobile-development': {
            'title': 'Mobile App Development with React Native',
            'description': 'Build cross-platform mobile applications using React Native. Create iOS and Android apps with a single codebase.',
            'price': '$179.00',
            'rating': 4.6,
            'students': 750,
            'duration': '14 weeks',
            'instructor': 'Sarah Wilson',
            'instructor_bio': 'Mobile Development Expert, Published 15+ apps on App Store',
            'total_lessons': 52,
            'total_hours': 42,
            'level': 'Intermediate',
            'language': 'English',
            'certificate': True,
            'lifetime_access': True
        },
        'cybersecurity': {
            'title': 'Cybersecurity Fundamentals & Ethical Hacking',
            'description': 'Learn cybersecurity principles, ethical hacking techniques, and how to secure systems against cyber threats.',
            'price': '$249.00',
            'rating': 4.8,
            'students': 650,
            'duration': '18 weeks',
            'instructor': 'Alex Rodriguez',
            'instructor_bio': 'Certified Ethical Hacker (CEH), Cybersecurity Consultant',
            'total_lessons': 68,
            'total_hours': 55,
            'level': 'Intermediate to Advanced',
            'language': 'English',
            'certificate': True,
            'lifetime_access': True
        }
    }
    
    # Получаем курс или используем web-design по умолчанию
    course = course_data.get(course_slug, course_data['web-design'])
    
    # Добавляем дополнительные данные для каждого курса
    course_levels = {
        'beginner': {
            'name': 'Beginner',
            'icon': 'fas fa-seedling',
            'color': 'success',
            'price': 'Free',
            'lessons': 12,
            'duration': '4 weeks',
            'description': 'Perfect for complete beginners with no prior experience',
            'unlocked': True
        },
        'medium': {
            'name': 'Medium',
            'icon': 'fas fa-chart-line', 
            'color': 'warning',
            'price': '$99',
            'lessons': 18,
            'duration': '6 weeks', 
            'description': 'For those with basic knowledge who want to advance',
            'unlocked': False
        },
        'advanced': {
            'name': 'Advanced',
            'icon': 'fas fa-rocket',
            'color': 'danger', 
            'price': '$199',
            'lessons': 25,
            'duration': '8 weeks',
            'description': 'Master level content for experienced developers',
            'unlocked': False
        }
    }
    
    # Тестовые отзывы
    testimonials = [
        {
            'name': 'Emma Johnson',
            'role': 'Frontend Developer at Microsoft',
            'rating': 5,
            'comment': 'This course completely changed my career! The instructor explains complex concepts in a very understandable way.',
            'avatar': 'testimonial-1.jpg'
        },
        {
            'name': 'David Kim', 
            'role': 'Full-Stack Developer',
            'rating': 5,
            'comment': 'Best investment I have ever made. Got a job as a developer within 3 months of completing the course.',
            'avatar': 'testimonial-2.jpg'
        },
        {
            'name': 'Maria Garcia',
            'role': 'Freelance Web Designer', 
            'rating': 4,
            'comment': 'Great content and practical projects. Really helped me build a strong portfolio.',
            'avatar': 'testimonial-3.jpg'
        }
    ]
    
    # FAQ данные
    faqs = [
        {
            'question': 'How long do I have access to the course?',
            'answer': 'You get lifetime access to all course materials, including future updates.'
        },
        {
            'question': 'Is there a money-back guarantee?',
            'answer': 'Yes! We offer a 30-day money-back guarantee if you are not satisfied with the course.'
        },
        {
            'question': 'Do I need any prior experience?',
            'answer': 'No prior experience is required for the beginner level. We start from the very basics.'
        },
        {
            'question': 'Will I get a certificate?',
            'answer': 'Yes, you will receive a certificate of completion that you can add to your LinkedIn profile.'
        }
    ]
    
    # Что студенты изучат
    learning_outcomes = [
        'Build responsive websites from scratch',
        'Master HTML5, CSS3, and JavaScript',
        'Work with modern frameworks like React',
        'Understand backend development with Node.js',
        'Deploy applications to the cloud',
        'Build a professional portfolio',
        'Get job-ready skills for web development',
        'Learn industry best practices and standards'
    ]
    
    context = {
        'course': course,
        'course_levels': course_levels,
        'testimonials': testimonials,
        'faqs': faqs,
        'learning_outcomes': learning_outcomes
    }  
    return render(request, 'course_detail.html', context)
