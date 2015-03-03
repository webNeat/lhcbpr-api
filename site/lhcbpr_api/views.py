from lhcbpr_api.models import (Application, ApplicationVersion,
                               Option, Attribute, SetupProject,
                               JobDescription,
                               AttributeThreshold, Handler, JobHandler,
                               HandlerResult, AddedResult, Job,
                               JobResult, ResultFile, Platform, Host)

from rest_framework import viewsets

from rest_framework.response import Response
from serializers import *
from rest_framework_extensions.mixins import NestedViewSetMixin
from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.decorators import detail_route, list_route


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationVersionViewSet(viewsets.ModelViewSet):
    queryset = ApplicationVersion.objects.all()
    serializer_class = ApplicationVersionSerializer


class OptionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class AttributeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeThresholdViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AttributeThreshold.objects.all()
    serializer_class = AttributeThresholdSerializer


class SetupProjectViewSet(viewsets.ModelViewSet):
    queryset = SetupProject.objects.all()
    serializer_class = SetupProjectSerializer


class JobDescriptionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer


class HandlerViewSet(viewsets.ModelViewSet):
    queryset = Handler.objects.all()
    serializer_class = HandlerSerializer


class JobHandlerViewSet(viewsets.ModelViewSet):
    queryset = JobHandler.objects.all()
    serializer_class = JobHandlerSerializer


class HandlerResultViewSet(viewsets.ModelViewSet):
    queryset = HandlerResult.objects.all()
    serializer_class = HandlerResultSerializer


class JobResultViewSet(viewsets.ModelViewSet):
    queryset = JobResult.objects.all()
    serializer_class = JobResultSerializer


class JobResultByOptionAndAttribute(viewsets.ViewSet):
    queryset = JobResult.objects.all()

    def list(self, request, option, attr):
        queryset = JobResult.objects.filter(
            job__job_description__option__pk=option, attr__pk=attr)
        serializer = JobResultSerializer(
            queryset, context={'request': request}, many=True)
        return Response(serializer.data)


class ResultFileViewSet(viewsets.ModelViewSet):
    queryset = ResultFile.objects.all()
    serializer_class = ResultFileSerializer


class JobViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class PlatformViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class HostViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer


class ActiveApplicationViewSet(viewsets.ViewSet):

    def list(self, request):
        id_field = 'job_description__application_version__application__id'
        name_field = 'job_description__application_version__application__name'
        queryset = (
            Job.objects
            .select_related()
            .values(id_field, name_field)
            .annotate(njobs=Count(id_field))
            .order_by(name_field)
        )
        result = []
        for app in queryset:
            result.append(
                {"id": app[id_field],
                 "name": app[name_field],
                 "count": app["njobs"]
                 }
            )
        serializer = ActiveItemSerializer(result, many=True, read_only=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Application.objects.all()
        app = get_object_or_404(queryset, pk=pk)
        serializer = ApplicationSerializer(app, context={'request': request})
        return Response(serializer.data)

    @list_route()
    def versions(self, request, pk):
        id_field = 'job_description__application_version__id'
        name_field = 'job_description__application_version__version'
        queryset = (
            Job.objects
            .select_related()
            .values(id_field, name_field)
            .filter(job_description__application_version__application__id=pk)
            .annotate(njobs=Count(id_field))
        )
        result = []
        for app in queryset:
            result.append(
                {"id": app[id_field],
                 "name": app[name_field],
                 "count": app["njobs"]
                 }
            )
        serializer = ActiveItemSerializer(result, many=True, read_only=True)
        return Response(serializer.data)

    @list_route()
    def options(self, request, pk):
        id_field = 'job_description__option__id'
        name_field = 'job_description__option__content'

        versions = []
        if 'versions' in request.query_params and request.query_params['versions']:
            versions = [
                int(v) for v in request.query_params['versions'].split(',')
            ]

        queryset = (Job.objects.select_related().values(id_field, name_field)
                    .filter(
                        job_description__application_version__application__id=pk
        ))
        if versions:
            queryset = queryset.filter(
                job_description__application_version__id__in=versions)
        queryset = queryset.annotate(njobs=Count(id_field))

        result = []
        for option in queryset:
            result.append(
                {"id": option[id_field],
                 "name": option[name_field],
                 "count": option["njobs"]
                 }
            )

        serializer = ActiveItemSerializer(result, many=True, read_only=True)
        return Response(serializer.data)


class SearchJobsViewSet(viewsets.ViewSet):

    def list(self, request):
        id_field = 'job_description__application_version__application__id'
        name_field = 'job_description__application_version__application__name'
        queryset = (
            Job.objects
            .select_related()
            .order_by("-id")
        )
        application = request.query_params.get("application", None)
        if application:
            ids = application.split(',')
            queryset = queryset.filter(
                job_description__application_version__application__id__in=ids)

        versions = request.query_params.get("versions", None)
        if versions:
            ids = versions.split(',')
            queryset = queryset.filter(
                job_description__application_version__id__in=ids)

        options = request.query_params.get("options", None)
        if options:
            ids = options.split(',')
            queryset = queryset.filter(job_description__option__id__in=ids)

        serializer = JobSerializer(queryset, many=True, read_only=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Job.objects.all()
        job = get_object_or_404(queryset, pk=pk)
        serializer = JobSerializer(job, context={'request': request})
        return Response(serializer.data)

    @list_route()
    def versions(self, request, pk):
        id_field = 'job_description__application_version__id'
        name_field = 'job_description__application_version__version'
        queryset = (
            Job.objects
            .select_related()
            .values(id_field, name_field)
            .filter(job_description__application_version__application__id=pk)
            .annotate(njobs=Count(id_field))
        )
        result = []
        for app in queryset:
            result.append(
                {"id": app[id_field],
                 "name": app[name_field],
                 "count": app["njobs"]
                 }
            )
        serializer = ActiveItemSerializer(result,many=True, read_only=True)
        return Response(serializer.data)

    @list_route()
    def options(self, request, pk):
        id_field = 'job_description__option__id'
        name_field = 'job_description__option__content'

        versions = []
        if 'versions' in request.query_params and request.query_params['versions']:
            versions = [
                int(v) for v in request.query_params['versions'].split(',')
            ]

        queryset = (Job.objects.select_related().values(id_field, name_field)
                    .filter(job_description__application_version__application__id=pk))
        if versions:
            queryset = queryset.filter(
                job_description__application_version__id__in=versions)
        queryset = queryset.annotate(njobs=Count(id_field))

        result = []
        for option in queryset:
            result.append(
                {"id": option[id_field],
                 "name": option[name_field],
                 "count": option["njobs"]
                 }
            )

        serializer = ActiveItemSerializer(result, many=True, read_only=True)
        return Response(serializer.data)
