from statistics import mode
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import profile

class BusinessType(models.Model):

    # Fields
    id = models.AutoField(primary_key=True)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("BusinessOwener_BusinessType_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("BusinessOwener_BusinessType_update", args=(self.id,))


class storeprofile(models.Model):

    # Fields
    user = models.ForeignKey(profile,on_delete=models.CASCADE)
    BID = models.BigAutoField(primary_key=True)
    BStoreName = models.CharField(max_length=50)
    
    BPinCode = models.PositiveIntegerField()
    BAddressLine1 = models.TextField(max_length=100)
    BAddressLine2 = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
    
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("BusinessOwener_storeprofile_detail", args=(self.BID,))

    def get_update_url(self):
        return reverse("BusinessOwener_storeprofile_update", args=(self.BID,))


class stroetiming(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    Time = models.DurationField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("BusinessOwener_stroetiming_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("BusinessOwener_stroetiming_update", args=(self.pk,))
