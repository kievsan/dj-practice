import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from random import choice

from students.models import Course, Student

URL = r'/api/v1/courses/'


def __get_data(url, client, params=None):
    response = client.get(url, data=params)
    data = response.json()
    return response.status_code, data


def __get_random_course_data(list_of_courses, name=None):
    random_course = choice(list_of_courses)
    if name:
        return random_course.name
    return random_course.id


@pytest.fixture
def url_factory():
    def factory(url, obj=None):
        if obj:
            url += f'{obj.id}/'
        return url
    return factory


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course():
    return baker.make(Course)


@pytest.fixture
def courses():
    return baker.make(Course, _quantity=30)


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_new_course(client, url_factory, course):
    status, data = __get_data(url_factory(URL, course), client)
    assert status == 200
    assert data['id'] == course.id


@pytest.mark.django_db
def test_get_list_of_courses(client, url_factory, courses):
    status, data = __get_data(url_factory(URL), client)
    for index, course in enumerate(data):
        assert course['id'] == courses[index].id
    assert status == 200


@pytest.mark.django_db
def test_course_filter_id(client, url_factory, courses):
    random_course_id = __get_random_course_data(courses)
    params = {'id': random_course_id}
    status, data = __get_data(url_factory(URL), client, params=params)
    assert data[0]['id'] == random_course_id
    assert status == 200


@pytest.mark.django_db
def test_course_filter_name(client, url_factory, courses):
    random_course_name = __get_random_course_data(courses, name=True)
    params = {'name': random_course_name}
    status, data = __get_data(url_factory(URL), client, params=params)
    assert data[0]['name'] == random_course_name
    assert status == 200


@pytest.mark.django_db
def test_course_create(client, url_factory):
    count = Course.objects.count()
    course_name = 'Python_course'
    data = {'name': course_name}
    response = client.post(url_factory(URL), data=data)
    new_course = Course.objects.filter(name=course_name)[0]
    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    assert new_course.name == course_name


@pytest.mark.django_db
def test_course_update(client, url_factory, course, student_factory):
    student = student_factory()
    len_before = len(course.students.all())
    data = {'students': [student.id]}
    response = client.patch(url_factory(URL, course), data=data)
    len_after = len(course.students.all())
    assert len_before == len_after - 1
    assert response.status_code == 200


@pytest.mark.django_db
def test_course_delete(client, url_factory, course):
    response = client.delete(url_factory(URL, course))
    deleted_course = Course.objects.filter(id=course.id)
    assert not deleted_course
    assert response.status_code == 204
