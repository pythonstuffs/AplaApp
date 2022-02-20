import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from Country_State_List import models as Country_State_List_models
from users import models as users_models
from BusinessOwener import models as BusinessOwener_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_Country_State_List_Country(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return Country_State_List_models.Country.objects.create(**defaults)
def create_Country_State_List_State(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["last_updated"] = datetime.now()
    defaults["id"] = "auto"
    defaults["name"] = "text"
    defaults["created"] = datetime.now()
    defaults.update(**kwargs)
    return Country_State_List_models.State.objects.create(**defaults)
def create_Country_State_List_City(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["created"] = datetime.now()
    defaults["id"] = "auto"
    defaults["last_updated"] = datetime.now()
    defaults["name"] = "text"
    defaults.update(**kwargs)
    return Country_State_List_models.City.objects.create(**defaults)
def create_Country_State_List_Locality(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults["name"] = "text"
    defaults["id"] = "auto"
    defaults["created"] = datetime.now()
    defaults["last_updated"] = datetime.now()
    defaults.update(**kwargs)
    return Country_State_List_models.Locality.objects.create(**defaults)
def create_users_profile(**kwargs):
    defaults = {}
    defaults["slug"] = ""
    defaults["MobileNumber"] = ""
    defaults["birthday"] = datetime.now()
    defaults["profileimage"] = ""
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return users_models.profile.objects.create(**defaults)
def create_BusinessOwener_BusinessType(**kwargs):
    defaults = {}
    defaults["name"] = ""
    defaults.update(**kwargs)
    return BusinessOwener_models.BusinessType.objects.create(**defaults)
def create_BusinessOwener_storeprofile(**kwargs):
    defaults = {}
    defaults["BPinCode"] = ""
    defaults["BAddressLine1"] = ""
    defaults["BAddressLine2"] = ""
    defaults["BStoreName"] = ""
    defaults["last_updated"] = datetime.now()
    defaults["id"] = "auto"
    defaults["name"] = "text"
    defaults["created"] = datetime.now()
    defaults["created"] = datetime.now()
    defaults["id"] = "auto"
    defaults["last_updated"] = datetime.now()
    defaults["name"] = "text"
    defaults["name"] = "text"
    defaults["id"] = "auto"
    defaults["created"] = datetime.now()
    defaults["last_updated"] = datetime.now()
    defaults["id"] = "auto"
    defaults["created"] = datetime.now()
    defaults["last_updated"] = datetime.now()
    defaults["name"] = "text"
    defaults["slug"] = "slug"
    defaults["created"] = datetime.now()
    defaults["MobileNumber"] = "text"
    defaults["birthday"] = datetime.now()
    defaults["profileimage"] = "anImage"
    defaults["last_updated"] = datetime.now()
    defaults["id"] = "auto"
    defaults["last_updated"] = datetime.now()
    defaults["name"] = "text"
    defaults["created"] = datetime.now()
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return BusinessOwener_models.storeprofile.objects.create(**defaults)
def create_BusinessOwener_stroetiming(**kwargs):
    defaults = {}
    defaults["Time"] = ""
    defaults["BID"] = "sometext"
    defaults["BPinCode"] = 1
    defaults["BAddressLine1"] = "text"
    defaults["last_updated"] = datetime.now()
    defaults["BAddressLine2"] = "text"
    defaults["BStoreName"] = "text"
    defaults["created"] = datetime.now()
    defaults.update(**kwargs)
    return BusinessOwener_models.stroetiming.objects.create(**defaults)
