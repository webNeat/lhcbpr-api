from lhcbpr_api.models import (Application, ApplicationVersion,
                               Option, Attribute, SetupProject,
                               JobDescription,
                               AttributeThreshold, Handler, JobHandler,
                               HandlerResult, AddedResult, Job,
                               JobResult, ResultFile)

from rest_framework import viewsets
from serializers import (ApplicationSerializer, ApplicationVersionSerializer,
                         OptionSerializer, AttributeSerializer,
                         SetupProjectSerializer,
                         JobDescriptionSerializer,
                         AttributeThresholdSerializer,
                         HandlerSerializer, JobHandlerSerializer,
                         HandlerResultSerializer, AddedResultSerializer,
                         JobSerializer,
                         JobResultSerializer, ResultFileSerializer)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationVersionViewSet(viewsets.ModelViewSet):
    queryset = ApplicationVersion.objects.all()
    serializer_class = ApplicationVersionSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeThresholdViewSet(viewsets.ModelViewSet):
    queryset = AttributeThreshold.objects.all()
    serializer_class = AttributeThresholdSerializer


class SetupProjectViewSet(viewsets.ModelViewSet):
    queryset = SetupProject.objects.all()
    serializer_class = SetupProjectSerializer


class JobDescriptionViewSet(viewsets.ModelViewSet):
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


class ResultFileViewSet(viewsets.ModelViewSet):
    queryset = ResultFile.objects.all()
    serializer_class = ResultFileSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
