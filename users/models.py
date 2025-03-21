from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='confirmation_code')
    code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.code}"
