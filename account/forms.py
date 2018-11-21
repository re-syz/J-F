"""
131072
221118 - initial
account/forms.py



"""


# =============

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)
