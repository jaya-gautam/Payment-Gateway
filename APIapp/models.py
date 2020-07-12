from django.db import models

# Create your models here.

class Card(models.Model):
    cc_number=models.CharField(max_length=100)
    expirationMonth=models.CharField(max_length=2)
    expirationYear=models.CharField(max_length=4)
    cvv=models.CharField(max_length=3)

    def __str__(self):
        return self.cc_number

class Transaction(models.Model):
    txn_id=models.CharField(max_length=12, blank=True, null=True)
    amount=models.CharField(max_length=20)
    currency=models.CharField(max_length=3)
    card_type=models.CharField(max_length=10,default='')
    card=models.ForeignKey(Card, related_name='transactions', on_delete=models.CASCADE)
    status=models.CharField(max_length=1000)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.txn_id

