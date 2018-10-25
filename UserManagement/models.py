from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.


class LookingForJob(models.Model):
    first_name = models.CharField(max_length=10, verbose_name="First Name")
    last_name = models.CharField(max_length=10, verbose_name="Last Name")
    phone_number = models.IntegerField(null=False, unique=True)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

    def clean(self):
        cleaned_data = super(LookingForJob, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError(
                "password and confirm_password does not match"
            )


