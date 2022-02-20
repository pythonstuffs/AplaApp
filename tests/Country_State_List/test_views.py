import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Country_list_view():
    instance1 = test_helpers.create_Country_State_List_Country()
    instance2 = test_helpers.create_Country_State_List_Country()
    client = Client()
    url = reverse("Country_State_List_Country_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Country_create_view():
    client = Client()
    url = reverse("Country_State_List_Country_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Country_detail_view():
    client = Client()
    instance = test_helpers.create_Country_State_List_Country()
    url = reverse("Country_State_List_Country_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Country_update_view():
    client = Client()
    instance = test_helpers.create_Country_State_List_Country()
    url = reverse("Country_State_List_Country_update", args=[instance.id, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_State_list_view():
    instance1 = test_helpers.create_Country_State_List_State()
    instance2 = test_helpers.create_Country_State_List_State()
    client = Client()
    url = reverse("Country_State_List_State_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_State_create_view():
    client = Client()
    url = reverse("Country_State_List_State_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_State_detail_view():
    client = Client()
    instance = test_helpers.create_Country_State_List_State()
    url = reverse("Country_State_List_State_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_State_update_view():
    client = Client()
    instance = test_helpers.create_Country_State_List_State()
    url = reverse("Country_State_List_State_update", args=[instance.id, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_City_list_view():
    instance1 = test_helpers.create_Country_State_List_City()
    instance2 = test_helpers.create_Country_State_List_City()
    client = Client()
    url = reverse("Country_State_List_City_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_City_create_view():
    client = Client()
    url = reverse("Country_State_List_City_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_City_detail_view():
    client = Client()
    instance = test_helpers.create_Country_State_List_City()
    url = reverse("Country_State_List_City_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_City_update_view():
    client = Client()
    instance = test_helpers.create_Country_State_List_City()
    url = reverse("Country_State_List_City_update", args=[instance.id, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Locality_list_view():
    instance1 = test_helpers.create_Country_State_List_Locality()
    instance2 = test_helpers.create_Country_State_List_Locality()
    client = Client()
    url = reverse("Country_State_List_Locality_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Locality_create_view():
    client = Client()
    url = reverse("Country_State_List_Locality_create")
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Locality_detail_view():
    client = Client()
    instance = test_helpers.create_Country_State_List_Locality()
    url = reverse("Country_State_List_Locality_detail", args=[instance.id, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Locality_update_view():
    client = Client()
    instance = test_helpers.create_Country_State_List_Locality()
    url = reverse("Country_State_List_Locality_update", args=[instance.id, ])
    data = {
        "name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302
