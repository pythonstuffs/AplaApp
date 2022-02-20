from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from BusinessOwener.models import storeprofile
from Product.models import Product
from users.models import profile
class PaymentStatus(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.AutoField(primary_key=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Transaction_PaymentStatus_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("Transaction_PaymentStatus_update", args=(self.id,))

class TransactionMode(models.Model):

    # Fields
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Transaction_TransactionMode_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("Transaction_TransactionMode_update", args=(self.id,))


class TransactionStatus(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    id = models.AutoField(primary_key=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Transaction_TransactionStatus_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("Transaction_TransactionStatus_update", args=(self.id,))

class Invoice(models.Model):

    # Fields
    TransactionStatus = models.ForeignKey(TransactionStatus,on_delete=models.CASCADE)
    TID = models.BigAutoField(primary_key=True)
    CID = models.ForeignKey(profile,on_delete=models.CASCADE)
    BID = models.ForeignKey(storeprofile,on_delete=models.CASCADE)
    BName = models.CharField(max_length=30)
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2)#Query Feild
    PTransactionMode = models.ForeignKey(TransactionMode,on_delete=models.CASCADE)
    PaymentStatus = models.ForeignKey(PaymentStatus,on_delete=models.CASCADE)
    TransactionDate = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Transaction_Invoice_detail", args=(self.TID,))

    def get_update_url(self):
        return reverse("Transaction_Invoice_update", args=(self.TID,))




class Order(models.Model):

    # Fields
    
    PName = models.CharField(max_length=30)
    OID = models.BigAutoField(primary_key=True)
    TID = models.ForeignKey(Invoice,on_delete=models.CASCADE)
    PID = models.ForeignKey(Product,on_delete=models.CASCADE)
    PUnit = models.DecimalField(max_digits=10,decimal_places=2)
    PPrice = models.DecimalField(max_digits=10,decimal_places=2)
    PTotal = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Transaction_Order_detail", args=(self.OID,))

    def get_update_url(self):
        return reverse("Transaction_Order_update", args=(self.OID,))
