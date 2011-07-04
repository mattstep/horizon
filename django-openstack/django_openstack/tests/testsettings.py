# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2011 United States Government as represented by the
# Administrator of the National Aeronautics and Space Administration.
# All Rights Reserved.
#
# Copyright 2011 Fourth Paradigm Development, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
TESTSERVER = 'http://testserver'
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/tmp/django-openstack.db',
            },
        }
INSTALLED_APPS = ['django.contrib.auth',
                  'django.contrib.contenttypes',
                  'django.contrib.sessions',
                  'django.contrib.sites',
                  'django_openstack',
                  'django_openstack.tests',
                  'django_openstack.templatetags',
                  'mailer',
                  ]
ROOT_URLCONF = 'django_openstack.tests.testurls'
TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'tests', 'templates')
)
SITE_ID = 1
SITE_BRANDING = 'OpenStack'
SITE_NAME = 'openstack'
ENABLE_VNC = True
NOVA_DEFAULT_ENDPOINT = None
NOVA_DEFAULT_REGION = 'test'
NOVA_ACCESS_KEY = 'test'
NOVA_SECRET_KEY = 'test'

CREDENTIAL_AUTHORIZATION_DAYS = 2
CREDENTIAL_DOWNLOAD_URL = TESTSERVER + '/credentials/'

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
NOSE_ARGS = ['--nocapture',
            ]

# django-mailer uses a different config attribute
# even though it just wraps django.core.mail
MAILER_EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
EMAIL_BACKEND = MAILER_EMAIL_BACKEND

