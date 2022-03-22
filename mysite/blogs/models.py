from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from accounts.models import CustomUser

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
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

    def get_absolute_url(self):
        return reverse('blogs:detail', kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.pk) + '-' + str(self.author))
        super(Blog, self).save(*args, **kwargs)
