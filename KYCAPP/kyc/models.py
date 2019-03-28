from django.db import models
import datetime
class Customer(models.Model):
    Customer_id = models.IntegerField()
    How = models.CharField(max_length=100, default='some string')
    Date = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    Comments = models.CharField(max_length=100, default='some string')
    Customer_number = models.IntegerField()
    Staff_user_id = models.IntegerField()
    Staff_name = models.CharField(max_length=100, default='some string')
    Satisfied = models.BooleanField()
    Bank_id = models.CharField(max_length=100, default='some string')

    def __str__(self):
        return str(self.Bank_id)