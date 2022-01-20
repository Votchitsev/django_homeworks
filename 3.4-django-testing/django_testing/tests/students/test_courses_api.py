import json

import pytest
from django.urls import reverse
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_first_course(course_factory, client):
    course_factory(_quantity=10)

    course_query = Course.objects.first()
    url = f"http://127.0.0.1:8000/api/v1/courses/{course_query.id}/"
    response = client.get(url)

    assert response.status_code == 200
    assert response.data['id'] == course_query.id
    assert response.data['name'] == course_query.name


@pytest.mark.django_db
def test_get_courses_list(course_factory, client):
    courses = course_factory(_quantity=20)

    url = reverse('courses-list')
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.data) == len(courses)

    for index, course in enumerate(response.data):
        assert courses[index].name == course['name']


@pytest.mark.django_db
def test_courses_list_filter(course_factory, client):
    course_factory(_quantity=20)
    course_for_filtering = Course.objects.first()
    url = f'http://127.0.0.1:8000/api/v1/courses/?id={course_for_filtering.id}'
    response = client.get(url)
    response_json = response.json()

    assert response.status_code == 200
    assert len(response_json) == 1
    assert response_json[0]['id'] == course_for_filtering.id
    assert response_json[0]['name'] == course_for_filtering.name


@pytest.mark.django_db
def test_courses_list_filter_by_name(course_factory, client):

    courses = course_factory(_quantity=20)
    course_name = courses[0].name
    url = f'http://127.0.0.1:8000/api/v1/courses/?name={course_name}'
    response = client.get(url)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json[0]['name'] == course_name


@pytest.mark.django_db
def test_creating_course(client):

    course_data = {
        "name": "Test_name"
    }

    data = json.dumps(course_data)

    url = "http://127.0.0.1:8000/api/v1/courses/"

    response = client.post(url, data=data, content_type="Application/json")

    assert Course.objects.filter(name=response.data['name'])
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(course_factory, client):

    course = course_factory()

    course_data_for_updating = {
        "name": "New_name"
    }

    course_data_for_updating_json = json.dumps(course_data_for_updating)

    url = f'http://127.0.0.1:8000/api/v1/courses/{course.id}/'

    response = client.patch(url, data=course_data_for_updating_json, content_type="Application/json")

    assert response.status_code == 200
    assert response.data['name'] == "New_name"


@pytest.mark.django_db
def test_delete_course(course_factory, client):

    course = course_factory()

    url = f"http://127.0.0.1:8000/api/v1/courses/{course.id}/"

    response = client.delete(url)

    assert response.status_code == 204
    assert client.get(url).status_code == 404
