import json
from pprint import pprint

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
    course = course_factory()
    url = reverse("courses-list")
    response = client.get(url)

    assert response.status_code == 200
    assert response.data[0]['id'] == course.id
    assert response.data[0]['name'] == course.name


@pytest.mark.django_db
def test_get_courses_list(course_factory, client):
    courses = course_factory(_quantity=20)
    url = reverse('courses-list')
    response = client.get(url)

    id_list_response = [i['id'] for i in response.data]
    id_list_db = [i.id for i in courses]
    id_set = set(id_list_response + id_list_db)

    name_list_response = [i['name'] for i in response.data]
    name_list_db = [i.name for i in courses]
    name_set = set(name_list_response + name_list_db)

    assert response.status_code == 200
    assert len(courses) == len(response.data)
    assert len(id_set) == 20
    assert len(name_set) == 20


@pytest.mark.django_db
def test_courses_list_filter(course_factory, client):

    def get_course(courses_list, course_id):
        for course in courses_list:
            if course.id == course_id:
                return course.name
            else:
                pass

    courses = course_factory(_quantity=20)
    url = 'http://127.0.0.1:8000/api/v1/courses/?id=25'
    response = client.get(url)
    response_json = response.json()

    course_name = get_course(courses, 25)

    assert response.status_code == 200
    assert len(response_json) == 1
    assert response_json[0]['id'] == 25
    assert response_json[0]['name'] == course_name


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
