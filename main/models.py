from django.db import models

class Investor(models.Model):
    icon = models.ImageField()

    class Meta():
        verbose_name = "Investor"
        verbose_name = "Investors table"


class Service(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.ImageField()

    def __str__(self):
        return self.title
    
    class Meta():
        verbose_name = "Service"
        verbose_name = "Services table"


class Leadership(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Leadership"
        verbose_name = "Leaderships table"


class Images_leadership(models.Model):
    image = models.ImageField()
    leadership_id = models.IntegerField()
    
    def __str__(self):
        return self.image
    
    class Meta():
        verbose_name = "Image leadership"
        verbose_name_plural = "Images leaderships"


class Social_media_link(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()
    path = models.TextField()
    leadership_id = models.IntegerField()

    def __str__(self):
        return self.path
    
    class Meta():
        verbose_name = "Social media link"
        verbose_name_plural = "Social media links"


class Testimonial(models.Model):
    body = models.TextField()


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    massage = models.TextField(null=True)

    def __str__(self):
        return self.first_name


# https://bootstraptema.ru/_sf/55/5560.html 