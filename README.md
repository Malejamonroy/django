# django

//ver version 
python -m django --version  


// crear entorno virtual
 python -m venv env
 .\env\Scripts\Activate, si da error ejecutar el siguiente:
 Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

// si no tienes instalado Con el entorno virtual activado, instala Django:
pip install django

// crear proyecto
python -m django startproject videoclub 

// crear directorio web para subaplicaciones
mkdir apps

// registrar apps del proyecto - settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo',
    'users',
]

// generar primera migración y base de datos
python manage.py migrate

// Configurar las URLs
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),  # Catálogo y alquiler
    path('users/', include('users.urls')),  # Login, registro, perfil
]

// run 
 python manage.py runserver            

// crear subprojectos:
  django-admin startapp catalogo web/catalogo


// vamos dentro de la estructura para crear el proyecto x
 C:\Users\xx\PROYECTOS\django\videoclub\web>  o 
python manage.py startapp catalogo web/catalogo

-----------------------
ESTRUCTURA BASE DE PROYECTO 

django/                   # Proyecto Django
│── manage.py                # Comando principal de Django
│── db.sqlite3               # Base de datos (puede ser MySQL o PostgreSQL)
│── requirements.txt         # Dependencias del proyecto
│── .env                     # Variables de entorno (opcional)
│
├── videoclub/               # Configuración del proyecto
│   │── __init__.py          # Indica que es un paquete de Python
│   │── settings.py          # Configuración general
│   │── urls.py              # Enlaces globales de la web
│   │── asgi.py              # ASGI (para WebSockets, etc.)
│   │── wsgi.py              # WSGI (para servidores web)
│
├── web/                     # Carpeta principal de la web
│   ├── catalogo/            # Aplicación del catálogo de películas
│   │   │── migrations/      # Migraciones de la base de datos
│   │   │── static/          # Archivos estáticos (CSS, JS, imágenes)
│   │   │   ├── catalogo/    # Archivos específicos de esta app
│   │   │       ├── styles.css  
│   │   │── templates/       # Plantillas HTML de la aplicación
│   │   │   ├── catalogo/
│   │   │       ├── catalogo.html
│   │   │── views.py         # Controladores de la vista
│   │   │── models.py        # Modelos de la base de datos
│   │   │── urls.py          # Enlaces específicos de esta app
│   │   │── forms.py         # Formularios de Django
│   │   │── admin.py         # Configuración del panel de administración
│   │   │── tests.py         # Pruebas unitarias
│   │   └── apps.py          # Configuración de la aplicación
│
│   ├── users/               # Aplicación de autenticación y usuarios
│   │   │── migrations/      # Migraciones de la base de datos
│   │   │── templates/       # Plantillas HTML de autenticación
│   │   │   ├── users/
│   │   │       ├── login.html
│   │   │       ├── register.html
│   │   │       ├── perfil.html
│   │   │── views.py         # Controladores de la vista
│   │   │── models.py        # Modelos de usuarios
│   │   │── urls.py          # Enlaces específicos de esta app
│   │   │── forms.py         # Formularios de Django
│   │   │── admin.py         # Configuración del panel de administración
│   │   │── tests.py         # Pruebas unitarias
│   │   └── apps.py          # Configuración de la aplicación
│
│── static/                  # Archivos estáticos globales
│   ├── images/              # Imágenes generales
│   ├── css/                 # Archivos CSS globales
│   ├── js/                  # Archivos JavaScript
│
│── templates/               # Plantillas HTML globales
│   ├── base.html            # Plantilla base para reutilizar
│
│── media/  