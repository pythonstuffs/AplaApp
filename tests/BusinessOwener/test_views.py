import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_BusinessType_list_view():
    instance1 = test_helpers.create_BusinessOwener_BusinessType()
    instance2 = test_helpers.create_BusinessOwener_BusinessType()
    client = Client()
    url = reverse("BusinessOwener_BusinessType_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_BusinessType_create_view():
    client = Client()
    url = reverse("BusinessOwener_BusinessType_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_BusinessType_detail_view():
    client = Client()
    instance = test_helpers.create_BusinessOwener_BusinessType()
    url = reverse("BusinessOwener_BusinessType_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_BusinessType_update_view():
    client = Client()
    instance = test_helpers.create_BusinessOwener_BusinessType()
    url = reverse("BusinessOwener_BusinessType_update", args=[instance.id, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_storeprofile_list_view():
    instance1 = test_helpers.create_BusinessOwener_storeprofile()
    instance2 = test_helpers.create_BusinessOwener_storeprofile()
    client = Client()
    url = reverse("BusinessOwener_storeprofile_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_storeprofile_create_view():
    client = Client()
    url = reverse("BusinessOwener_storeprofile_create")
    data = {
        "BPinCode": 1,
        "BAddressLine1": "text",
        "BAddressLine2": "text",
        "BStoreName": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_storeprofile_detail_view():
    client = Client()
    instance = test_helpers.create_BusinessOwener_storeprofile()
    url = reverse("BusinessOwener_storeprofile_detail", args=[instance.BID, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_storeprofile_update_view():
    client = Client()
    instance = test_helpers.create_BusinessOwener_storeprofile()
    url = reverse("BusinessOwener_storeprofile_update", args=[instance.BID, ])
    data = {
        "BPinCode": 1,
        "BAddressLine1": "text",
        "BAddressLine2": "text",
        "BStoreName": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_stroetiming_list_view():
    instance1 = test_helpers.create_BusinessOwener_stroetiming()
    instance2 = test_helpers.create_BusinessOwener_stroetiming()
    client = Client()
    url = reverse("BusinessOwener_stroetiming_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_stroetiming_create_view():
    client = Client()
    url = reverse("BusinessOwener_stroetiming_create")
    data = {
        "Time": 1.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_stroetiming_detail_view():
    client = Client()
    instance = test_helpers.create_BusinessOwener_stroetiming()
    url = reverse("BusinessOwener_stroetiming_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_stroetiming_update_view():
    client = Client()
    instance = test_helpers.create_BusinessOwener_stroetiming()
    url = reverse("BusinessOwener_stroetiming_update", args=[instance.pk, ])
    data = {
        "Time": 1.0,
    }
    response = client.post(url, data)
    assert response.status_code == 302
