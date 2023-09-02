from django.db import models

# Create your models here.

ROLES_CHOICES = (
    ('pm', 'pm'),
    ('sd', 'sd'),
    ('da', 'da'),
    ('et', 'et'),
    ('ma', 'ma'),

)
roles_shortcut = {
    'sd': "Django Backend Developer",
    'pm': "Product Manager",
    'da': "Data Analyist",
    'et': "Entrepreneur",
    'ma': "Social Media Specialist"
}

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    url = models.URLField()
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Work(models.Model):
    company = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    start_year = models.PositiveSmallIntegerField()
    end_year = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    skills = models.ManyToManyField(Skill)
    def __str__(self):
        return self.title + " at " + self.company

class Role(models.Model):
    # Text
    abb = models.CharField(max_length=2, choices=ROLES_CHOICES)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    slogan = models.CharField(max_length=150)

    # Colors
    first_color = models.CharField(max_length=7)
    second_color = models.CharField(max_length=7)
    third_color = models.CharField(max_length=7)

    img = models.ImageField(upload_to='images/')

    projects = models.ManyToManyField(Project)
    works = models.ManyToManyField(Work)

    def __str__(self):
        return self.name
    








