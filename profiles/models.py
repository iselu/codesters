from django.db import models
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

class Student(models.Model):
    user = models.ForeignKey(User)
    bio = models.TextField(blank=True, default='')
    github_username = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    twitter_username = models.CharField(max_length=30, null=True, blank=True)
    stackoverflow = models.URLField(null=True, blank=True)
    coderwall = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
#    badges = models.ManyToManyField('tracks.Badge', null=True, blank=True)
#    chapters_completed = models.ManyToManyField('tracks.Chapter', null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('student_detail', kwargs={'pk': self.id})
