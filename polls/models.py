from django.db import models
from audit_log.models.managers import AuditLog


# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200)

class Project(models.Model):
    name = models.CharField(max_length=200)
    group = models.OneToOneField(Group)
    audit_log = AuditLog()
