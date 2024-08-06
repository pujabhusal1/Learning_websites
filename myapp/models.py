from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)  # Consider changing the max_length
    desc = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # Automatically set the date and time when the record is created

    def __str__(self):
        return self.name
