
import pytest

from faker import Faker
from core.http_client import HttpClient


@pytest.mark.api1
def test_get_users_info():
    fake = Faker()
    body = {
  "username": fake.user_name(),
  "email": fake.email(),
  "password": "Qwerty123"
    }
    url = '/auth/register'
    
    response = HttpClient().post(url=url, body= body)
    
    access_token = response["access_token"]

    url = '/users/?skip=0&limit=100'

    headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
           }

    response = HttpClient().get(url=url, headers=headers)

    assert response    

@pytest.mark.api2
def test_update_user():
    body = {
  "email": "admin@example.com",
  "password": "admin123"
    }   
    url = "/auth/login"

    response = HttpClient().post(url=url, body=body)
    access_token = response["access_token"]

    url = "/users/2"
    fake = Faker()
    body = {
  "username": fake.user_name(),
  "email": "fake@gmail.com",
  "role": "user",
  "avatar_url": "string"
    }

    headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json",
            "Content-Type": "application/json"
    }
    response = HttpClient().put(url=url, body=body, headers=headers)

    assert response["username"] == body["username"]
    assert response["email"] == body["email"]

@pytest.mark.api3
def test_delete_user():
    body = {
  "email": "admin@example.com",
  "password": "admin123"
    }   
    url = "/auth/login"

    response = HttpClient().post(url=url, body=body)
    access_token = response["access_token"]

    url = '/users/?skip=0&limit=100'

    headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
           }

    response_get_users = HttpClient().get(url=url, headers=headers)

    url = "/users/10"

    headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "*/*"
    }

    response = HttpClient().delete(url=url, headers=headers)

    assert response_get_users[9]["id"] != 10

@pytest.mark.api4
def test_search_tasks():
    body = {
  "email": "admin@example.com",
  "password": "admin123"
    }
    url = "/auth/login"

    response = HttpClient().post(url=url, body=body)
    access_token = response["access_token"]  
    
    body = {
  "title": "test1",
  "description": "string",
  "status": "todo",
  "priority": "medium",
  "assignee_id": 2
    }
    url = '/boards/2/tasks'
    headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json",
            "Content-Type": "application/json"
    }    
    response = HttpClient().post(url=url, body=body, headers=headers)
    len_tasks_before = len(response)
    url = '/tasks/search?q=test1&skip=0&limit=100'

    headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json"
   }

    response = HttpClient().get(url=url, headers=headers)
    len_tasks_after_create = len(response)
    assert len_tasks_after_create == len_tasks_before  

@pytest.mark.api5
def test_create_task():
    body = {
  "email": "admin@example.com",
  "password": "admin123"
    }
    url = "/auth/login"

    response = HttpClient().post(url=url, body=body)
    access_token = response["access_token"]  
    
    body = {
  "title": "test1",
  "description": "string",
  "status": "todo",
  "priority": "medium",
  "assignee_id": 2
    }
    url = '/boards/2/tasks'
    headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json",
            "Content-Type": "application/json"
    }    
    response = HttpClient().post(url=url, body=body, headers=headers)
    assert response['title'] == body['title']
    assert response['description'] == body['description']
    assert response['status'] == body['status']

@pytest.mark.api6
def test_delete_task():
    body = {
  "email": "admin@example.com",
  "password": "admin123"
    }
    url = "/auth/login"

    response = HttpClient().post(url=url, body=body)
    access_token = response["access_token"]  
    body = {
  "title": "test1",
  "description": "string",
  "status": "todo",
  "priority": "medium",
  "assignee_id": 2
    }
    url = '/boards/2/tasks'
    headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "application/json",
            "Content-Type": "application/json"
    }    
    response = HttpClient().post(url=url, body=body, headers=headers)

    url = '/boards/2/tasks/575'
    headers = {
            "Authorization": f"Bearer {access_token}",
            "accept": "*/*",
    }    
    response = HttpClient().delete(url=url, headers=headers)
    assert response is None