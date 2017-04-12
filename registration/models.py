from django.db import models


#
# # Create your models here.
class Cookie(models.Model):
    enrollment = models.CharField(max_length=10)
    cookie = models.CharField(max_length=1000)

    def __str__(self):
        return str(self.enrollment)