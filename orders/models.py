from django.db import models
from django.utils import timezone

class Order(models.Model):
    
    NEW = 'N'
    INPROGRESS = 'IP'
    LAYOUTREADY = 'LR'
    DONE = 'D'
    ORDER_STATUSES = [
        (NEW, 'New'),
        (LAYOUTREADY, 'Layout ready'),
        (INPROGRESS, 'In progress'),
        (DONE, 'Done'),
    ]

    order_name = models.CharField(max_length=100)
    customer = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    status = models.CharField(max_length=15, choices=ORDER_STATUSES,default=NEW)
    add_date = models.DateTimeField(auto_now_add=True, editable=False)
    deadline_date = models.DateField('Deadline')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.order_name

    def days_left(self):       
        return self.deadline_date - self.add_date.date()