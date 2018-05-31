from django.db import models

# Create your models here.

class AsyncMember(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

class AsyncOrder(models.Model):
    order_id = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
