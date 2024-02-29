# def test_example():
#     assert False, "Just test example"
from random import randint

import pytest

url_local = '/api/v1/courses/'

#Сравнение списков
@pytest.mark.django_db
def test_courses_list(client, courses_factory):
    response_get = client.get(url_local)

    assert response_get.status_code == 200
    data = response_get.json()
    assert len(data) == len(courses_factory)


@pytest.mark.django_db
def test_course(client, course):
    response_get = client.get(f'{url_local}{course.id}/')
    response_post = client.post('/api/v1/courses/', data={'name': 'Python',})


    assert response_get.status_code == 200
    assert response_post.status_code == 201
    data = response_post.json()
    assert data['name'] == 'Python'

@pytest.mark.django_db
def test_filter_id(client,courses_factory):

    random_id = [i.id for i in courses_factory][randint(0, 9)]
    response_get = client.get(f'{url_local}?id={random_id}')

    assert response_get.status_code == 200
    assert response_get.data[0]['id'] == random_id

@pytest.mark.django_db
def test_filter_name(client, courses_factory):

    random_name = [i.name for i in courses_factory][randint(0, 9)]
    response_get = client.get(f'{url_local}?name={random_name}')

    assert response_get.status_code == 200
    assert response_get.data[0]['name'] == random_name

@pytest.mark.django_db
def test_update(client, course):

    response_get_old = client.get(f'{url_local}{course.id}/')
    response_put = client.put(f'{url_local}{course.id}/', data={'name': 'JS'})
    response_get_new = client.get(f'{url_local}{course.id}/')

    assert response_get_old.status_code == 200
    assert response_put.status_code == 200
    assert response_get_old.json() != response_get_new.json()

@pytest.mark.django_db
def test_delete(client, course):

    response_get_old = client.get(f'{url_local}{course.id}/')
    response_delete = client.delete(f'{url_local}{course.id}/')
    response_get_new = client.get(f'{url_local}{course.id}/')

    assert response_get_old.status_code == 200
    assert response_delete.status_code == 204
    assert len(response_get_old.json()) != len(response_get_new.json())