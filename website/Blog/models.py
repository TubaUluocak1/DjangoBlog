from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()


class Contact(models.Model):
    İsim = models.CharField(max_length=150)
    Email = models.EmailField()
    Mesaj = models.TextField()

    def __str__(self):
        return self.İsim

class Slider(models.Model):
    image = models.ImageField(upload_to="images/%y/%m/%d/")

class Author(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="")
 
    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"    

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    thumbnail = models.ImageField(upload_to="",null=True,blank=True)
    image_url = models.CharField(max_length=500,default=None,null=True,blank=True)
    overview = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    content = RichTextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    published = models.BooleanField()
    
    def __str__(self):
        return self.title