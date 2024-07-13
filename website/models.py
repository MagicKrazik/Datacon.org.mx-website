from django.db import models

# Create your models here.
    
class QuoteRequest(models.Model):
       name = models.CharField(max_length=100)
       email = models.EmailField()
       phone = models.CharField(max_length=20, blank=True)
       company = models.CharField(max_length=100, blank=True)
       industry = models.CharField(max_length=100, blank=True)
       project_type = models.CharField(max_length=100)
       project_description = models.TextField()
       budget = models.CharField(max_length=50, blank=True)
       timeline = models.CharField(max_length=100, blank=True)
       services = models.CharField(max_length=255, blank=True)  # Store as comma-separated values
       additional_info = models.TextField(blank=True)
       created_at = models.DateTimeField(auto_now_add=True)

       def __str__(self):
           return f"Quote Request from {self.name} - {self.created_at}"    
       

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    company = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    language = models.CharField(max_length=50, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.created_at}"       