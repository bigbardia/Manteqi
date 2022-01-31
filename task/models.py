from django.db import models

class Task(models.Model):

    session_id = models.CharField(max_length=2000000000000)
    title = models.TextField()
    done = models.BooleanField(default=False)
    is_edited = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
