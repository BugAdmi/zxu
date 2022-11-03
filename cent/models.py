from django.db import models

# Create your models here.

class CentView(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField(verbose_name="年龄")

    class Meta:
        db_table = "cent"
