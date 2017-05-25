from django.core.management.base import BaseCommand
from main_app.models import Work, Hobby, Study
from datetime import date


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):

        works = [
            {'organization': 'СПБ ГБУ ГОРЖИЛОБМЕН', 'region': 'Санкт-Петербург', 'site': 'obmencity.ru',
             'position': '"Сервис инженер по информационным системам"',
             'duties': 'Защита информации, издание ключей ЭЦП, хелпдеск, удалённая настройка рабочих мест'},
            {'organization': 'ЧтоДелатьКонсалт', 'region': 'Санкт-Петербург', 'site': '4dk.ru',
             'position': '"Менеджер по продажам"',
             'duties': 'Консультирование и продажа ПО Консультант+'},
            {'organization': 'Буквоед', 'region': 'Санкт-Петербург', 'site': 'bookvoed.ru',
             'position': '"Бариста"',
             'duties': 'Приготовление вкуснейшего кофе и чая в ночное время'}
        ]
        hobbies = [
            {'hobby_name': 'Кулинария', 'hobby_desc': 'Выпечка кексиков'},
            {'hobby_name': 'Python', 'hobby_desc': 'Создание нейросетей'},
            {'hobby_name': 'Django', 'hobby_desc': 'Создание динамичных сайтов'},
            {'hobby_name': 'Припарирование одноклеточных', 'hobby_desc': 'Что-то из раздела биологии'},

        ]
        studies = [
            {'place_of_study': 'Обучающий портал GeekBrains:',
             'discipline': '"Программист Python"'},
            {'place_of_study': 'СПб ГУТД',
             'discipline': '"Финансы и кредит"'},
            {'place_of_study': 'ЧОУ ДПО "Формула защиты:',
             'discipline': '"Информационная безопасность"'},
            {'place_of_study': 'Колледж "СТАНКОЭЛЕКТРОН:',
             'discipline': '"Бух.учёт, анализ, аудит"'},
        ]

        Work.objects.all().delete()
        for work in works:
            work = Work(**work)
            work.save()

        Hobby.objects.all().delete()
        for hobby in hobbies:
            hobby = Hobby(**hobby)
            hobby.save()

        Study.objects.all().delete()
        for study in studies:
            study = Study(**study)
            study.save()
