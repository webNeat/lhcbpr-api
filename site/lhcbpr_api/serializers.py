from lhcbpr_api.models import (Application, ApplicationVersion, Option,
                               SetupProject, JobDescription, Attribute,
                               AttributeThreshold, Handler, HandlerResult,
                               JobHandler, AddedResult, Job,
                               JobResult, ResultFile)
from rest_framework import serializers


class OptionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Option
        fields = ('content', 'description', 'is_standalone')


class SetupProjectSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = SetupProject
        fields = ('content', 'description')


class JobDescriptionSerializer(serializers.HyperlinkedModelSerializer):
    # application_version = ApplicationVersionSerializer(many=False)
    option = OptionSerializer(many=False)
    setup_project = SetupProjectSerializer(many=False)

    class Meta:
        model = JobDescription
        fields = ('application_version', 'setup_project', 'option')


class ApplicationVersionSerializer(serializers.HyperlinkedModelSerializer):
    job_descriptions = JobDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = ApplicationVersion
        fields = ('application', 'version', 'job_descriptions')


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    # versions = serializers.StringRelatedField(many=True)
    versions = ApplicationVersionSerializer(many=True, read_only=True)

    class Meta:
        model = Application
        fields = ('name', 'versions')


class AttributeThresholdSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AttributeThreshold
        fields = ('attribute', 'up_value', 'down_value', 'start')


class AttributeSerializer(serializers.HyperlinkedModelSerializer):
    thresholds = AttributeThresholdSerializer(many=True, read_only=True)

    class Meta:
        model = Attribute
        fields = ('name', 'dtype', 'description', 'thresholds')


class JobDescriptionSerializer(serializers.HyperlinkedModelSerializer):
    # application_version = ApplicationVersionSerializer(many=False)
    # option = OptionSerializer(many=False)
    # setup_project = SetupProjectSerializer(many=True, read_only=True)

    class Meta:
        model = JobDescription
        fields = ('application_version', 'setup_project', 'option')


class HandlerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Handler
        fields = ('name', 'description')


class JobHandlerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = JobHandler
        fields = ('job_description', 'handler')


class HandlerResultSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = HandlerResult
        fields = ('job', 'handler', 'is_success')


class AddedResultSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = AddedResult
        fields = ('identifier')


class JobResultSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = JobResult
        fields = ('job', 'attr', 'data')


class ResultFileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = JobResult
        fields = ('job', 'file')

class JobSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Job
        fields = ('host', 'platform', 'time_start',
            'time_end', 'status', 'is_success')
