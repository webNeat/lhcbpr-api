from lhcbpr_api.models import (Application, ApplicationVersion, Option,
                               SetupProject, JobDescription, OptionAttribute, AttributeThreshold)
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
    jobdescriptions = JobDescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = ApplicationVersion
        fields = ('application', 'version', 'jobdescriptions')


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


class OptionAttributeSerializer(serializers.HyperlinkedModelSerializer):
    thresholds = AttributeThresholdSerializer(many=True, read_only=True)

    class Meta:
        model = OptionAttribute
        fields = ('option', 'name', 'dtype', 'description', 'thresholds')


class JobDescriptionSerializer(serializers.HyperlinkedModelSerializer):
    # application_version = ApplicationVersionSerializer(many=False)
    # option = OptionSerializer(many=False)
    # setup_project = SetupProjectSerializer(many=True, read_only=True)

    class Meta:
        model = JobDescription
        fields = ('application_version', 'setup_project', 'option')

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
