from django.db import models
from django.urls import reverse


class Country(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Country_State_List_Country_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("Country_State_List_Country_update", args=(self.id,))


class State(models.Model):

    # Fields
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Country_State_List_State_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("Country_State_List_State_update", args=(self.id,))


class City(models.Model):

    # Fields
    id = models.AutoField(primary_key=True)
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Country_State_List_City_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("Country_State_List_City_update", args=(self.id,))


class Locality(models.Model):

    # Fields
    City = models.ForeignKey(City,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("Country_State_List_Locality_detail", args=(self.id,))

    def get_update_url(self):
        return reverse("Country_State_List_Locality_update", args=(self.id,))
