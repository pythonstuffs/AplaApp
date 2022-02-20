import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_profile_list_view():
    instance1 = test_helpers.create_users_profile()
    instance2 = test_helpers.create_users_profile()
    client = Client()
    url = reverse("users_profile_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_profile_create_view():
    client = Client()
    url = reverse("users_profile_create")
    data = {
        "slug": "slug",
        "MobileNumber": "text",
        "birthday": datetime.now(),
        "profileimage": "anImage",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_profile_detail_view():
    client = Client()
    instance = test_helpers.create_users_profile()
    url = reverse("users_profile_detail", args=[instance.slug, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_profile_update_view():
    client = Client()
    instance = test_helpers.create_users_profile()
    url = reverse("users_profile_update", args=[instance.slug, ])
    data = {
        "slug": "slug",
        "MobileNumber": "text",
        "birthday": datetime.now(),
        "profileimage": "anImage",
    }
    response = client.post(url, data)
    assert response.status_code == 302
