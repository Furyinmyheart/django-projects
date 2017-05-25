from django.shortcuts import render, render_to_response
from .models import Work
from .models import Study
#from .models import Hobby

# Create your views here.

def index_view(request):
    name = 'Михаил'
    surname = 'Андриченко'
    nickname = 'Sladeomfg'
    birthday_date = '22 ноября 1993 г.'
    family = 'не женат'
    my_hobby = [
        'Кулинария',
        'Python',
        'Django',
        'Припарирование одноклеточных'
    ]
    work_places = Work.objects.all()
    study_places = Study.objects.all()
    return render(request, 'index.html', {'name': name, 'surname': surname, 'nickname': nickname,
                                             'birthday_date': birthday_date, 'family': family, 'my_hobby': my_hobby,
                                             'work_places': work_places, 'study_places': study_places },)


#   def study_view(request):
#       study_places = [
#           {'name': 'Обучающий портал GeekBrains:',
#            'education': '"Программист Python"'},
#           {'name': 'СПб ГУТД',
#            'education': '"Финансы и кредит"'},
#           {'name': 'ЧОУ ДПО "Формула защиты:',
#            'education': '"Информационная безопасность"'},
#           {'name': 'Колледж "СТАНКОЭЛЕКТРОН:',
#            'education': '"Бух.учёт, анализ, аудит"'},
#       ]
#       return render_to_response('study.html', {'study_places': study_places})
#
#
#   def job_view(request):
#       work_places = [
#
#           {'name': 'СПБ ГБУ ГОРЖИЛОБМЕН:',
#            'post': '"Сервис инженер по информационным системам"'},
#           {'name': 'ЧтоДелатьКонсалт:',
#            'post': '"Менеджер по продажам"'},
#           {'name': 'Буквоед:',
#            'post': '"Бариста"'},
#           {'name': 'Спортмастер:',
#            'post': '"Продавец консультант"'},
#       ]
#       return render_to_response('job.html', {'work_places': work_places})


def contacts_view(request):
    phone = '+7(999)214-90-70'
    email = 'Bokohod@bk.ru'
    map = '<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d1993.1772216352006!2d30.29855231633023!3' \
          'd60.028714981909076!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4696345f32ad7dc5%3A0x6b0ef7d1eb2b1c0' \
          'a!2z0YPQuy4g0KnQtdGA0LHQsNC60L7QstCwLCA0LCDQodCw0L3QutGCLdCf0LXRgtC10YDQsdGD0YDQsywgMTk3Mzc1!5e0!3m2!1sru!2s' \
          'ru!4v1494422909431" width="470" height="450" frameborder="0" style="border:0" allowfullscreen></iframe>'
    return render(request, 'contacts.html', {'phone': phone, 'email': email, 'map': map})


#def hobby_view(request):
#    hobbys = Hobby.objects.all()
#    return render_to_response("index.html", {'hobbys': hobbys})

def auth_view(request):
    return render(request, "auth.html")