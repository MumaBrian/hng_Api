from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Api(models.Model):
    # title = models.CharField(max_length=100)
    # memo = models.TextField(blank=True)
    # created = models.DateTimeField(auto_now_add=True)
    # datecompleted = models.DateTimeField(null=True, blank=True)
    # important = models.BooleanField(default=False)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    slackUsername=models.CharField(max_length=100)
    backend=models.BooleanField(default=False)
    age=models.IntegerField()
    bio=models.CharField(max_length=250)

    def __str__(self):
        return self.slackUsername
