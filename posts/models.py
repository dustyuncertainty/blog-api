from django.db import models
from django.conf import settings

class Posts(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    
    # 1. Creation time (set only once)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # 2. Update time (changes every time the object is saved)
    updated_at = models.DateTimeField(auto_now=True) # <--- Added
    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    def __str__(self):
        return self.title