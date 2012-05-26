from django.db import models
from django.contrib.auth.models import User


class Password(models.Model):
    """
    Represents a username and password together with several other fields
    """
#    owner = models.ForeignKey(User, related_name='created_by',
#        editable=False)
    title = models.CharField(max_length=200)
    username = models.CharField(max_length=200,
        blank=True)
    password = models.CharField(max_length=200)
    url = models.URLField(max_length=500,
        blank=True,
        verbose_name='Site URL')
    notes = models.CharField(
        max_length=500,
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return self.title
