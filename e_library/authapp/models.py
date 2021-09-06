from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserProfile(AbstractUser):
    img = models.ImageField(verbose_name="Фото", upload_to='users_photo', blank=True)

    GENDER_MAN = 'm'
    GENDER_WOMAN = 'w'
    GENDER_CHOICES = (
        (GENDER_MAN, _('Мужчина')),
        (GENDER_WOMAN, _('Женщина')),
    )
    gender = models.CharField(_('gender'), max_length=1,
                              choices=GENDER_CHOICES, blank=True)
