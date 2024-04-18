from django.db import models
from django.contrib.auth.models import AbstractUser
from . managers import CustomUserManager
from django.utils import timezone

class User(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    team = models.ForeignKey(User, related_name='services_offered', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Technician(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15) 
    email = models.EmailField(max_length=255)  
    picture = models.ImageField(upload_to='technician_pictures/', blank=True, null=True)  
    skills = models.CharField(max_length=255) 

    def __str__(self):
        return self.name


class TechnicalRequest(models.Model):
    STATUS_CHOICES = (
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Conversation(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class FileAttachment(models.Model):
    support_request = models.ForeignKey(TechnicalRequest, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    support_request = models.OneToOneField(TechnicalRequest, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(default=timezone.now)

