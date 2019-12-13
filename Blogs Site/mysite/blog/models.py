from django.db import models
# from ckeditor.fields import RichTextField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    title = models.CharField(max_length= 30)

    def __str__(self):
        return self.title


class Post(models.Model):
    id_no = models.AutoField(primary_key= True)
    title = models.CharField(max_length = 180)
    content = models.TextField() 
    thumbnail = models.ImageField(upload_to='media/images')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length = 80)
    timestamp = models.DateTimeField(blank= True)
    description = models.TextField(max_length = 500)
    category = models.ManyToManyField(Category)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title