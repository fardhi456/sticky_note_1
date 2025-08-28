from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoTask(models.Model): 
    index = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=512)
    describtion = models.TextField(blank=True, null= True)
    due_date = models.DateField()
    created_at = models.DateField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id)
    
class StickyNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]