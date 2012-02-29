#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import sys
from optparse import OptionParser

from django.conf import settings

if not settings.configured:
    PROJECT_DIR, MODULE_NAME = os.path.split(
        (os.path.realpath(__file__))
    )

    settings.configure(
        DATABASE_ENGINE='sqlite3',
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                },
            },
        ROOT_URLCONF = 'videopages.urls',
        NOSE_ARGS = ['--nocapture',
                     '--all-modules',
                     '--nologcapture',
                     '--verbosity=2',
                     '--with-coverage',
                     '--cover-package=videopages',
                     '--cover-html',
                     #             '--with-doctest',
                     'videopages'
                     #             '--cover-erase',
                     #             '--cover-tests',
        ],
        TEMPLATE_CONTEXT_PROCESSORS = (
            'django.contrib.auth.context_processors.auth',
            'django.core.context_processors.debug',
            'django.core.context_processors.i18n',
            'django.core.context_processors.media',
            'django.core.context_processors.static',
            'django.core.context_processors.request',
        ),
        MIDDLEWARE_CLASSES = (
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
        ),
        TEMPLATE_LOADERS = (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ),
        TEMPLATE_DIRS = (
            os.path.join(PROJECT_DIR, 'videopages', 'tests', 'templates'),
        ),
        SITE_ID = 1,
        INSTALLED_APPS=[
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
            'django.contrib.messages',
            'tagging',
            'catalogs',
            'videopages',
            'djangovideos',
        ],
        DEBUG=False,
    )


from django_nose import NoseTestSuiteRunner

def runtests(*test_args, **kwargs):
    if not test_args:
        test_args = ['videopages']

    test_runner = NoseTestSuiteRunner(**kwargs)
    failures = test_runner.run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--verbosity', dest='verbosity', action='store', default=1, type=int)
    parser.add_options(NoseTestSuiteRunner.options)
    (options, args) = parser.parse_args()

    runtests(*args, **options.__dict__)