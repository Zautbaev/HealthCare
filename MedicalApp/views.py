from django.shortcuts import render  # Импорт стандартной функции для рендеринга шаблонов (здесь не используется)
from rest_framework import viewsets  # Импорт viewset'ов из Django REST Framework для создания API
from rest_framework.response import Response  # Импорт Response для отправки HTTP-ответов

from MedicalApp.models import Company  # Импорт модели Company, которая представляет данные компаний в базе данных
from MedicalApp.serializer import CompanySerializer  # Импорт сериализатора для модели Company
from rest_framework.generics import get_object_or_404


# Класс, представляющий API для работы с данными о компаниях
class CompanyViewSet(viewsets.ViewSet):

    # Метод для получения списка всех компаний (обрабатывает GET-запросы)
    def list(self, request):
        # Получаем все записи из модели Company
        company = Company.objects.all()
        # Сериализуем данные компаний в JSON формат, добавляя контекст с запросом
        serializer = CompanySerializer(company, many=True, context={'request': request})
        # Формируем словарь с ответом: статус ошибки, сообщение и сериализованные данные компаний
        response_dict = {'error': False, "message": 'All company list data', 'data': serializer.data}
        # Возвращаем ответ с данными
        return Response(response_dict)

    # Метод для создания новой компании (обрабатывает POST-запросы)
    def create(self, request):
        try:
            # Сериализуем данные из запроса
            serializer = CompanySerializer(data=request.data, context={'request': request})
            # Проверяем валидность данных
            serializer.is_valid()
            # Сохраняем данные в базу данных, если они валидны
            serializer.save()
            # Формируем успешный ответ
            dict_response = {'error': False, 'message': 'Company data save successfully'}
        except:
            # Если возникла ошибка при сохранении, возвращаем сообщение об ошибке
            dict_response = {'error': False, 'message': 'Error during saving company data'}
        # Возвращаем ответ
        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(company, data=request.data, context={'request':request})
            serializer.is_valid()
            serializer.save()
            dict_response = {'error':False, 'message': 'Success during updating company data'}

        except:
            dict_response = {'error':True, 'message': 'Error during updating company data'}

        return Response(dict_response)


# Создаем маршруты для работы с API
# company_list будет обрабатывать GET-запросы и вызывать метод list для получения списка компаний
company_list = CompanyViewSet.as_view({'get': 'list'})

# company_create будет обрабатывать POST-запросы и вызывать метод create для добавления новой компании
company_create = CompanyViewSet.as_view({'post': 'create'})

company_update = CompanyViewSet.as_view({'put':'update'})
