from datetime import timedelta
from secrets import token_urlsafe

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


# Create your models here.


class Profile(models.Model):
    birthday = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True, verbose_name="Аватар")
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                verbose_name="Пользователь",
                                related_name="profile")


class Token(models.Model):
    TOKEN_LIFETIME_SECONDS = 2 * 60 * 60

    token = models.CharField(max_length=50, unique=True, default=token_urlsafe)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def is_expired(self):
        return self.created_at + timedelta(seconds=self.TOKEN_LIFETIME_SECONDS) < timezone.now()

