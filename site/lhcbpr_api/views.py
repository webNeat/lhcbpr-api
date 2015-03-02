from lhcbpr_api.models import (Application, ApplicationVersion,
                               Option, Attribute, SetupProject,
                               JobDescription,
                               AttributeThreshold, Handler, JobHandler,
                               HandlerResult, AddedResult, Job,
                               JobResult, ResultFile, Platform, Host)

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from serializers import (ApplicationSerializer, ApplicationVersionSerializer,
                         OptionSerializer, AttributeSerializer,
                         SetupProjectSerializer,
                         JobDescriptionSerializer,
                         AttributeThresholdSerializer,
                         HandlerSerializer, JobHandlerSerializer,
                         HandlerResultSerializer, AddedResultSerializer,
                         JobSerializer,
                         JobResultSerializer, ResultFileSerializer,
                         PlatformSerializer, HostSerializer)
from rest_framework_extensions.mixins import NestedViewSetMixin

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationVersionViewSet(viewsets.ModelViewSet):
    queryset = ApplicationVersion.objects.all()
    serializer_class = ApplicationVersionSerializer


class OptionViewSet(NestedViewSetMixin,viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class AttributeViewSet(NestedViewSetMixin,viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeThresholdViewSet(NestedViewSetMixin,viewsets.ModelViewSet):
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
        queryset = JobResult.objects.filter(job__job_description__option__pk=option, attr__pk=attr)
        serializer = JobResultSerializer(queryset, context={'request': request}, many=True)
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
