from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.IntegerField()
    group = models.CharField(max_length=100)
    pay_status = models.BooleanField()

    def __str__(self):
        return f'{self.name} - {self.group}'

    def get_absolute_url(self):
        return self.pk
