"""
Django settings for FirstDjango project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1@7%gctoy&(ub-j2u20*i%8s$=+@bpj_*5q%#p++*wo_ic)$6$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'blog',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware', #启用伪post验证，ajax post就提交不了报403
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.transaction.TransactionMiddleware', #django.db.transaction事务支持
]

ROOT_URLCONF = 'FirstDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'FirstDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': '123xxx45',
        'HOST': 'localhost',
        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'  #引用名

#STATICFILES_DIRS
STATICFILES_DIRS = (
   os.path.join(BASE_DIR, 'statics/'),
    os.path.join(BASE_DIR, 'blog/static/'),
)
"""
    #注意1:
        #为了后端的更改不会影响前端的引入，避免造成前端大量修改

        STATIC_URL = '/statics/'               #引用名
        STATICFILES_DIRS = (
            os.path.join(BASE_DIR,"statics")  #实际名 ,即实际文件夹的名字
        )

        #django对引用名和实际名进行映射,引用时,只能按照引用名来,不能按实际名去找
        #<script src="/statics/jquery-3.1.1.js"></script>
        #------error－－－－－不能直接用，必须用STATIC_URL = '/statics/':
        #<script src="/statics/jquery-3.1.1.js"></script>

    #注意2(statics文件夹写在不同的app下,静态文件的调用):

        STATIC_URL = '/statics/'

        STATICFILES_DIRS=(
            (os.path.join(BASE_DIR,"app01","statics")) ,
        )

        #html中引用方式一
        #<script src="/statics/jquery-3.1.1.js"></script>

    #注意3:
        STATIC_URL = '/statics/'
        #html中引用方式二
        {% load staticfiles %}
        #<script src={% statics "jquery-3.1.1.js" %}></script>
"""