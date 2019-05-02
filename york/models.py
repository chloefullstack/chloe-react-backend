from django.db import models

# Create your models here.
class PuppyInfo(models.Model):
    profile_image = models.ImageField(default='static/images/default.jpg', upload_to='static/images')
    name = models.CharField(max_length=20, null=True, blank=True)
    sex = models.CharField(max_length=6, null=True, blank=True)
    age = models.CharField(max_length=2, null=True, blank=True)
    description = models.TextField(max_length=2000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
<<<<<<< HEAD

=======
    
    def save(self, *args, **kwargs):
        self.age = int(self.age) * 10
        super(PuppyInfo,self).save(*args, **kwargs)
>>>>>>> d194a7b31b93e27fec547caac6f5881ac03b53bb
