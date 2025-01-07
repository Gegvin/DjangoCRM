DjangoCRM — это простое пет-CRM-приложение на Django, позволяющее управлять 
заказами (Orders), сотрудниками (Staff) и выполнять базовую аналитику (Analytics).
Я тренировался создавать и использовать собственные API в данном случае DRF 
В приложении есть 2 основных приложение crm и analytics, они никак не связаны, только
тем, что находятся в одном django проекте. Analytics получается всю информацию по api



Основные Компоненты
	1.	Приложение crm
	•	Модель Order: хранит информацию о заказе (кофе, сироп, статус оплаты, цена и т. д.).
	•	ViewSet OrderViewSet: эндпоинт API (использует Django REST Framework) для CRUD-операций над заказами.
	•	Функции custom_order_list, create_order, mark_paid, delete_order: обычные Django-вьюхи для HTML-страниц, где пользователи могут просматривать, создавать, оплачивать или удалять заказы.
	2.	Приложение analytics
	•	Функция dashboard: отображает аналитику по заказам (количество, общий доход, распределение по типу кофе/сиропа).
	•	Функция get_orders() (в utils.py): через HTTP-запрос к эндпоинту /orders/ получает список заказов (JSON), а потом обрабатывает/группирует данные (например, с помощью pandas).
	3.	Django REST Framework
	•	Даёт набор API-эндпоинтов для работы с заказами и сотрудниками.
	•	Пример эндпоинтов (автоматически сформированных роутером в crm.urls):
	•	/orders/ (GET: список заказов, POST: создать заказ)
	•	/orders/<id>/ (GET, PUT, PATCH, DELETE)
	•	/staff/ (аналогично для сотрудников)

Основные URL
	1.	Главный urls.py (корень проекта):
 •	"/admin/" — стандартная админка Django.
	•	"/"       — ссылки из CRM/urls.py.
	•	"/analytics/" — ссылки из analytics/urls.py.

 	2.	crm/urls.py:
  •	/orderss/ (список HTML)
	•	/orderss/create/ (форма для создания заказа)
	•	/orderss/<id>/paid/ (отметить оплачено)
	•	/orderss/<id>/delete/ (удалить неоплаченный заказ)
	•	/orders/ (API эндпоинт, см. DRF Router)
	•	/orders/<id>/ (API CRUD, DRF)

 	3.	analytics/urls.py:
  •	/analytics/dashboard/: HTML-страница с аналитикой заказов.

  Установка и Запуск

  1.	Клонировать репозиторий:
git clone <URL_на_ваш_репозиторий>.git
cd DjangoCRM

 2.	Создать и активировать виртуальное окружение
python -m venv .venv
source .venv/bin/activate     # (Linux/Mac)
.venv\Scripts\activate        # (Windows)

 3.	Установить зависимости:
pip install -r requirements.txt

4.	Запуск миграций:
python manage.py makemigrations
python manage.py migrate

5.	Создать суперпользователя (для админки):
python manage.py createsuperuser

6. Создать Токен:

python manage.py drf_create_token <имя_пользователя>

7.	Создать файл .env в корне проекта (рядом с manage.py)
      и добавить в него переменные окружения:
  	
SECRET_KEY="django-insecure-..."
API_BASE_URL="http://127.0.0.1:8000/"
API_TOKEN="your_api_token"

8. Запустить сервер Django:
python manage.py runserver

9. Перейти в браузере на http://127.0.0.1:8000/.
