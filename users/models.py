import datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User,AbstractUser

class profile(AbstractUser):

    # Fields
    #user = models.ForeignKey(User,on_delete=models.CASCADE)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    MobileNumber = models.CharField(max_length=13)
    birthday = models.DateField(default=datetime.date.today())
    profileimage = models.ImageField(upload_to="upload/profileimages/")
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("users_profile_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("users_profile_update", args=(self.slug,))
