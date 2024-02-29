import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user('admin')

@pytest.fixture
def student():
    return baker.make(Student)

@pytest.fixture
def course():
    return baker.make(Course)

@pytest.fixture
def students_factory():
    return baker.make(Student, _quantity=10)


@pytest.fixture
def courses_factory():
    return baker.make(Course, _quantity=10)