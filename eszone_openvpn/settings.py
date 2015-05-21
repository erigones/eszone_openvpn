"""
Django settings for eszone_openvpn project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2@!^#^vn0j_g9i%w1udok7e8nax-+r$pv6yx$g(f#+us!0tq#*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django.contrib.admindocs',
    'api_openvpn',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'eszone_openvpn.urls'

WSGI_APPLICATION = 'eszone_openvpn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

VPN_PATHS = {
    'easy-rsa_path': '/etc/openvpn/easy-rsa',
    'openVPN-path': '/etc/openvpn',
    'log-path': '/var/log'
}

VPN_VARS = {
    'EASY_RSA': VPN_PATHS['easy-rsa_path'],
    'OPENSSL': 'openssl',
    'PKCS11TOOL': 'pkcs11-tool',
    'GREP': 'grep',
    'KEY_DIR': VPN_PATHS['easy-rsa_path'] + '/keys',
    'PKCS11_MODULE_PATH': 'dummy',
    'PKCS11_PIN': 'dummy',
    'KEY_NAME': 'EasyRSA',
}

#default values for vars
VPN_DEFAULT_VARS = {
    'KEY_SIZE': '512',      #2024 is recomended
    'CA_EXPIRE': '3650',
    'KEY_EXPIRE': '3650',
    'KEY_COUNTRY': 'SK',
    'KEY_PROVINCE': 'CA',
    'KEY_CITY': 'SK',
    'KEY_ORG': 'ORG',
    'KEY_EMAIL': 'vpn@vpn.com',
}

OPENVPN_COMMANDS = {
    'run-server': 'openvpn {file}',     # this is using for testing specific config
    'start': '/etc/init.d/openvpn start',
    'stop': '/etc/init.d/openvpn stop',
    'reload': '/etc/init.d/openvpn reload',
    'restart': '/etc/init.d/openvpn restart',
    'status': '/etc/init.d/openvpn status',
}

HELP_VARS = {
    'testing_ip': '127.0.0.1'   # loopback interface is remocmmended
}

