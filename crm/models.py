from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    insta = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(models.Model):
    NEW = 'New'
    INPROGRESS = 'In progress'
    LAYOUTREADY = 'Layout ready'
    DONE = 'Done'
    ORDER_STATUSES = [
        (NEW, 'New'),
        (LAYOUTREADY, 'Layout ready'),
        (INPROGRESS, 'In progress'),
        (DONE, 'Done'),
    ]

    name = models.CharField(max_length=100)
    desc = models.TextField('Description', blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=15, choices=ORDER_STATUSES, default=NEW)
    add_date = models.DateTimeField(auto_now_add=True, editable=False)
    deadline_date = models.DateField('Deadline')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def days_left(self):
        return self.deadline_date - timezone.now().date()

