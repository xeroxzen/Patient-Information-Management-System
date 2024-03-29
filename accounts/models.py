from django.db import models

# Create your models here.
from django.core.validators import RegexValidator

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

USERNAME_REGEX = '^[a-zA-Z0-9.+-]*$'

AUTHORISED_PERSONNEL = [
    ('Medical Doctor', 'Doctor'),
    ('Nurse', 'Nurse'),
    ('Secretary', 'Secretary'),
    ('Department of Health Rep', 'Health Officer')
]

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username = username,
            email = self.normalize_email(email),
            # role = 'Admin',
            # unique_id = '12345ABX-0',
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username,
            email,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    username = models.CharField(
                    max_length=255,
                    validators = [
                        RegexValidator(regex = USERNAME_REGEX,
                                message = 'Username must be alphanumeric or contain numbers',
                                code = 'invalid username'

                        )],
                     unique = True
                )

    email = models.EmailField(
        max_length=255,
        unique= True,
        verbose_name='email address'
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']


    def __str__(self):
        return self.username     #email initial

    def get_short_name(self):
        # The user is identified by their email address
        return self.username #email initially

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_perms(self, perms, obj=None):
        "Does the user have specific permission"
        # Yes
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'"
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        verbose_name_plural = "Admin"
        ordering = ("-username",)
