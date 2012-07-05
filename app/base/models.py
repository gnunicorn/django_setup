from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile



class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='my_profile')


