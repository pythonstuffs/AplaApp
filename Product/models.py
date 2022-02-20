from django.db import models
from django.urls import reverse
from BusinessOwener.models import storeprofile

class Product_Category(models.Model):

    # Fields
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Product_Product_Category_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("Product_Product_Category_update", args=(self.id,))


class Product_SubCategory(models.Model):

    # Fields
    
    Product_Category = models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    is_active = models.BooleanField(default=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Product_Product_SubCategory_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("Product_Product_SubCategory_update", args=(self.id,))


class Product(models.Model):

    # Fields
    PID = models.AutoField(primary_key=True)
    BID = models.ForeignKey(storeprofile,on_delete=models.CASCADE)
    PName = models.CharField(max_length=30)
    PCategory = models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    PSubCategory = models.ForeignKey(Product_SubCategory,on_delete=models.CASCADE)
    PSellingPrice = models.DecimalField(max_digits=10, decimal_places=2)
    PActualPrice = models.DecimalField(max_digits=10, decimal_places=2)
    PMargin = models.DecimalField(max_digits=10, decimal_places=2)
    PUnit = models.PositiveIntegerField()
    PAvailiblity = models.BooleanField(default=True)
    PDelivery = models.BooleanField(default=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    
    #POnBoardDate = models.DateTimeField(auto_now=True,editable=False)
    PImage = models.ImageField(upload_to="upload/images/")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Product_Product_detail", args=(self.PID,))

    def get_update_url(self):
        return reverse("Product_Product_update", args=(self.PID,))
