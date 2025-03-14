from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.admin.models import LogEntry



class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("L'utilisateur doit avoir un email")
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)  # Hash du mot de passe
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(username, email, password)
        user.is_admin = True
        user.is_active = True
        user.is_staff = True  # Ajout obligatoire
        user.is_superuser = True  # Ajout obligatoire
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)  # L'utilisateur doit activer son compte
    is_admin = models.BooleanField(default=False)  # Rôle administrateur
    is_staff = models.BooleanField(default=False)  # Champ obligatoire pour Django admin
    is_superuser = models.BooleanField(default=False)  # Django l’utilise pour les superutilisateurs

    groups = models.ManyToManyField(
        'auth.Group', related_name='custom_user_groups', blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_permissions', blank=True
    )

    objects = UserManager()  # Utilisation du manager personnalisé

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username
    
    def delete(self, *args, **kwargs):
        # Supprime d'abord les logs liés à cet utilisateur
        LogEntry.objects.filter(user_id=self.id).delete()
        super().delete(*args, **kwargs)


    @property
    def is_staff(self):
        return self.is_admin