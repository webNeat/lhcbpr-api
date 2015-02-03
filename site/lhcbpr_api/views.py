from lhcbpr_api.models import (Application, ApplicationVersion,
                               Option, OptionAttribute, SetupProject,
                               JobDescription,
                               AttributeThreshold)

from rest_framework import viewsets
from serializers import (ApplicationSerializer, ApplicationVersionSerializer,
                         OptionSerializer, OptionAttributeSerializer,
                         SetupProjectSerializer,
                         JobDescriptionSerializer,
                         AttributeThresholdSerializer)


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ApplicationVersionViewSet(viewsets.ModelViewSet):
    queryset = ApplicationVersion.objects.all()
    serializer_class = ApplicationVersionSerializer


class OptionViewSet(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer


class OptionAttributeViewSet(viewsets.ModelViewSet):
    queryset = OptionAttribute.objects.all()
    serializer_class = OptionAttributeSerializer


class AttributeThresholdViewSet(viewsets.ModelViewSet):
    queryset = AttributeThreshold.objects.all()
    serializer_class = AttributeThresholdSerializer


class SetupProjectViewSet(viewsets.ModelViewSet):
    queryset = SetupProject.objects.all()
    serializer_class = SetupProjectSerializer


class JobDescriptionViewSet(viewsets.ModelViewSet):
    queryset = JobDescription.objects.all()
    serializer_class = JobDescriptionSerializer
