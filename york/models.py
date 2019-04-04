from django.db import models

# Create your models here.
class PuppyInfo(models.Model):
    profile_image = models.ImageField(default='static/images/default.jpg', upload_to='static/images')
    name = models.CharField(max_length=20, null=True, blank=True)
    sex = models.CharField(max_length=6, null=True, blank=True)
    age = models.CharField(max_length=15, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name