from django.db import models

# Create your models here.


class Skills(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    score = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    def __str__(self):
        return f'{self.title} - {self.score}/100'

class About(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    avatar = models.ImageField(upload_to='about', null=True, blank=True)
    skills = models.ManyToManyField(Skills)

    class Meta:
        verbose_name_plural = 'Abouts'
        verbose_name = 'About'

    def __str__(self):
        return f'{self.name}'
