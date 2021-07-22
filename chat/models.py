from django.db import models

class Message(models.Model):
    room = models.CharField(max_length=255)
    username = models.CharField(max_length=30)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.room
        
    class Meta:
        ordering = ('date_added',)