from django.core.management.base import BaseCommand, CommandError
from lhcbpr_api.models import (Application, ApplicationVersion, SetupProject, Option, JobDescription,
                               Attribute, AttributeThreshold, Job)
from django.utils import timezone


class Command(BaseCommand):
    help = 'Fill initial data'

    def handle(self, *args, **options):

        gauss_app = Application(name='Gauss')
        brunel_app = Application(name='Brunel')

        gauss_app.save()
        brunel_app.save()

        v1 = ApplicationVersion(application=gauss_app, version='v1r0')
        v2 = ApplicationVersion(application=gauss_app, version='v2r0')
        v3 = ApplicationVersion(application=brunel_app, version='v1r0')
        v1.save()
        v2.save()
        v3.save()

        setup1 = SetupProject(
            content='--no-user-area', description='some description')
  
        opt1 = Option(
            content='my_option.py', description='run my option', is_standalone=False)
        opt2 = Option(content='my_standalone_option.py',
                      description='run my standalone option', is_standalone=True)
        setup1.save()
        opt1.save()
        opt2.save()
  
        
        jd1 = JobDescription(
            setup_project=setup1, application_version=v1, option=opt1)
        jd2 = JobDescription(
            setup_project=setup1, application_version=v1, option=opt2)
        jd3 = JobDescription(
            setup_project=setup1, application_version=v2, option=opt1)
        jd4 = JobDescription(
            setup_project=setup1, application_version=v3, option=opt1)
        jd1.save()
        jd2.save()
        jd3.save()
        jd4.save()

        a1 = Attribute(name="timer", dtype='float', description="My timer")
        a1.save()

        at1 = AttributeThreshold(option=opt1, attribute=a1, down_value=0,
                                 up_value=2, start=timezone.now())
        at1.save()
