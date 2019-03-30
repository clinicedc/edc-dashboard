#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname


app_name = 'edc_dashboard'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    template_dirs=[os.path.join(
        base_dir, app_name, "tests", "templates")],
    APP_NAME=app_name,
    BASE_DIR=base_dir,
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    INSTALLED_APPS=[
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'django_js_reverse',
        'django_crypto_fields.apps.AppConfig',
        'django_revision.apps.AppConfig',
        'edc_appointment.apps.AppConfig',
        'edc_base.apps.AppConfig',
        'edc_consent.apps.AppConfig',
        'edc_device.apps.AppConfig',
        'edc_identifier.apps.AppConfig',
        'edc_metadata.apps.AppConfig',
        'edc_model_wrapper.apps.AppConfig',
        'edc_navbar.apps.AppConfig',
        'edc_protocol.apps.AppConfig',
        'edc_registration.apps.AppConfig',
        'edc_timepoint.apps.AppConfig',
        'edc_visit_schedule.apps.AppConfig',
        'edc_visit_tracking.apps.AppConfig',
        'edc_dashboard.apps.AppConfig',
    ],
    add_dashboard_middleware=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    failures = DiscoverRunner(failfast=True).run_tests(
        [f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == '__main__':
    logging.basicConfig()
    main()