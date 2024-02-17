from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    id = id
    title = models.CharField(max_length=255)
    content = models.TextField()
    shared_users = models.ManyToManyField(User, related_name='shared_notes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title