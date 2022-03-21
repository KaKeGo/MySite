from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify

from accounts.models import CustomUser

# Create your models here.


class Contact(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    body = models.TextField()

    class Meta:
        verbose_name_plural = 'Contacts'
        verbose_name = 'Contact'

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    body = models.TextField()
    postman = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Contact messages'
        verbose_name = 'Contact message'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contacts:contact', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ContactMessage, self).save(*args, **kwargs)
