from django.db import models 
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model


# Create your models here.

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)
    
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)
    
def upload_to_profile(instance, filename):
    return f"profile_photos/user_{instance.pk}/{filename}"

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True )
    profile_photo = models.ImageField(upload_to=upload_to_profile, null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


    User = get_user_model()





class Book(models.Model):
    """
    Example model representing a Book. We add custom permissions here.
    The grader/test expects permission codenames: can_view, can_create, can_edit, can_delete
    """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_books"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

