from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100, blank=True, default="CHARLÈNE MORABITO")
    slogan = models.CharField(max_length=255, blank=True, default="SAVOIR-FAIRE ITALIEN, ALLURE PARISIENNE")
    call_to_action = models.CharField(max_length=100, blank=True, default="DÉCOUVRIR LA COLLECTION")

    def __str__(self):
        return self.name



class FirstHomeSection(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    link_text = models.CharField(max_length=100, blank=True)
    link_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='home/first_section/', blank=True, null=True)

    def __str__(self):
        return self.title or "Première section"


class SecondHomeSection(models.Model):
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    link_text = models.CharField(max_length=100, blank=True)
    link_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='home/second_section/', blank=True, null=True)

    def __str__(self):
        return self.title or "Deuxième section"
