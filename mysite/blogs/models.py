from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from accounts.models import CustomUser
from ckeditor.fields import RichTextField

from accounts.models import CustomUser

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blogs:detail', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Blog(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    category = models.CharField(max_length=100)
    likes = models.ManyToManyField(CustomUser, related_name='blog_like', blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    create_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_on = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['-create_on']
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'

    def __str__(self):
        return self.title + str(self.author)

    @property
    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('blogs:detail', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.pk) + '-' + str(self.author))
        super(Blog, self).save(*args, **kwargs)
