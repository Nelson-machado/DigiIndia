1.	What the project does?
DigiIndia, is an image based, corona statistics python Django project. The Main objective of this project was to learn and implement the usage of the APIs in the Django template.

2.	Why the project is useful?
The website is a one stop for your quick reference of the corona statistics in the state wise order.

3.	How users can get started with the project?

	To start the project
Django-admin startptoject DigiIndia

	To create the app:
Python manage.py startapp mapper

	To do an initial setup
Python manage.py migrate

	Add the template settings in the project folder’s settings.py file. And create the templates directory at the project level.
	TEMPLATES = [
	    {
	        'BACKEND': 'django.template.backends.django.DjangoTemplates',
	        'DIRS': [os.path.join(BASE_DIR, 'templates')],
	        'APP_DIRS': True,
	        'OPTIONS': {
	            'context_processors': [
	                'django.template.context_processors.debug',
	                'django.template.context_processors.request',
	                'django.contrib.auth.context_processors.auth',
	                'django.contrib.messages.context_processors.messages',
	            ],
	        },
	    },
	]


	Create the index.html page under the template directory.

	Add the mapper app’s url under main project’s url. Also, in settings.py add your app(mapper) under installed apps.




DigiIndia/Urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mapper.urls'))
]


DigiIndia/Settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mapper.apps.MapperConfig',
]


	Add the path to your index page in mapper/urls.py. Create the view in the Mapper/views.py page (this will contain the logic to read the api and send the data in the Django dictionary format to be read at Django template, i.e. index.html.

	from django.urls import path
	from mapper import views
	
	urlpatterns = [
	    path('', views.home, name='home')
	]


	Requests library is needed to get the responses from the api call.
Pip install requests

	Run below to see your result on the webpage(localhost):
Python manage.py runserver


 

 
 

 
