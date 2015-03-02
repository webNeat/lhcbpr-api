from django.db import models


DATA_TYPE_CHOICES = (
    ('str', 'string'),
    ('float', 'float'),
    ('int', 'integer'),
    ('dt', 'datetime')
)


class Host(models.Model):
    hostname = models.CharField(max_length=50)
    cpu_info = models.CharField(max_length=200)
    memory_info = models.CharField(max_length=200)

    def __unicode__(self):
        return self.hostname


class Application(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __unicode__(self):
        return '{0}'.format(self.name)


class ApplicationVersion(models.Model):
    application = models.ForeignKey(
        Application, related_name='versions', db_index=False
    )
    version = models.CharField(max_length=50)

    class Meta:
        unique_together = ("application", "version")

    def __unicode__(self):
        return '{0} {1}'.format(self.application.name, self.version)


class Option(models.Model):
    content = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)
    is_standalone = models.BooleanField(default=False)

    def __unicode__(self):
        return self.description


class SetupProject(models.Model):
    content = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.description


class JobDescription(models.Model):
    application_version = models.ForeignKey(
        ApplicationVersion, related_name='job_descriptions', db_index=False)
    option = models.ForeignKey(
        Option, null=True, related_name='job_descriptions', db_index=False)
    setup_project = models.ForeignKey(
        SetupProject, null=True, related_name='job_descriptions', db_index=False
    )

    def __unicode__(self):
        return '{0} (id)   {1}  {2}  {3}'.format(
            self.id,
            self.application_version.version,
            self.application_version.application.name,
            self.option.description
        )


class Platform(models.Model):
    cmtconfig = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.cmtconfig


class RequestedPlatform(models.Model):
    job_description = models.ForeignKey(JobDescription, db_index=False)
    cmtconfig = models.ForeignKey(Platform, db_index=False)

    class Meta:
        unique_together = ("job_description", "cmtconfig")

    def __unicode__(self):
        return '{0} (job_description_id)   ---   {1}'.format(
            self.job_description.id, self.cmtconfig
        )


class Job(models.Model):
    host = models.ForeignKey(
        Host, null=True, related_name='job', db_index=False)
    job_description = models.ForeignKey('JobDescription', related_name='jobs',
                                        db_column='job_description_id')
    platform = models.ForeignKey(Platform, null=True, related_name='jobs')
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    status = models.CharField(max_length=50)
    is_success = models.BooleanField(default=False)

    def results(self):
        return self.floats + self.string + self.integers

    def __unicode__(self):
        return '{0} (id) -- {1} (job_description_id)  ---  {2}  ---  {3}'\
               '  ---  {4} --- {5}'.format(
                   self.id, self.job_description.id, self.time_end,
                   self.platform.cmtconfig, self.host.hostname, self.is_success
               )


class Handler(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class JobHandler(models.Model):
    job_description = models.ForeignKey(JobDescription, db_index=False)
    handler = models.ForeignKey(Handler, db_index=False)

    class Meta:
        unique_together = ("job_description", "handler")

    def __unicode__(self):
        return '{0} (job_description_id) -- -- {1}'.format(
            self.job_description.id, self.handler
        )


class Attribute(models.Model):
    name = models.CharField(max_length=500, unique=True)
    dtype = models.CharField(max_length=8, choices=DATA_TYPE_CHOICES)
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return '{0} (id)  {1}  --  {2}  {3}'.format(
            self.id, self.name, self.dtype, self.description
        )


class AttributeThreshold(models.Model):
    attribute = models.ForeignKey(
        Attribute, related_name='thresholds', db_index=False
    )
    option = models.ForeignKey(
        Option, related_name='thresholds'
    )
    down_value = models.FloatField()
    up_value = models.FloatField()
    start = models.DateTimeField()


class JobResult(models.Model):
    job = models.ForeignKey(Job, related_name='results', db_index=False)
    attr = models.ForeignKey(
        Attribute, related_name='jobresults', db_index=False)
    handler = models.ForeignKey(Handler, related_name="results")
    val_float = models.FloatField(null=True)
    val_string = models.CharField(null=True, max_length=100)
    val_int = models.IntegerField(null=True)

    def __unicode__(self):
        return '{0} (job_id) --- {1}'.format(
            self.job.id, self.job_attribute
        )


# custom path to save the files in format
# MEDIA_ROOT/job_description_id/job_id/filename

# custom path to save the files in format
# MEDIA_ROOT/job_description_id/job_id/filename


def content_file_name(instance, filename):
    return '/'.join([str(instance.job.job_description.pk), str(instance.job.pk), filename])


class ResultFile(models.Model):
    job = models.ForeignKey(Job, related_name='files')
    file = models.FileField(upload_to=content_file_name, blank=True)

    def __unicode__(self):
        return '{0} (job_id) --- {1}'.format(
            self.job.id, self.file
        )


class HandlerResult(models.Model):
    job = models.ForeignKey(Job, db_index=False)
    handler = models.ForeignKey(Handler, db_index=False)
    is_success = models.BooleanField(default=False)

    def __unicode__(self):
        return '{0} (job_id) {1} --- {2}'.format(
            self.job.id, self.handler.name, self.is_success
        )


class AddedResult(models.Model):
    identifier = models.CharField(max_length=64)

    def __unicode__(self):
        return self.identifier
