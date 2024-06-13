from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    use_in_migrations = True
    def _create_user(self, phone_number, national_id ,email, password, **extra_fields):
        if not phone_number:
            raise ValueError("The given phone_number must be set")
        if self.model.objects.filter(phone_number=phone_number).exists():
            raise ValueError("phone number already exist")
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, national_id=national_id, email=email, **extra_fields)
        
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, national_id, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, national_id, email, password, **extra_fields)

    def create_superuser(self, phone_number, national_id, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phone_number, national_id, email, password, **extra_fields)



class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, verbose_name='username', null=True, unique=False)
    phone_number = models.CharField(max_length=15, verbose_name='phone_number', null=False, unique=True, db_index=True)
    national_id = models.CharField(max_length=10, verbose_name='national_id', null=False, unique=False, db_index=True)
    full_name = models.CharField(max_length=75, verbose_name='full_name', null=True)


    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["national_id"]

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
    


