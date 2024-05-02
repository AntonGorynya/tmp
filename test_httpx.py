import pytest
import httpx
from unittest.mock import ANY
from pytest_httpx import HTTPXMock


def test_404(httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        status_code=404,
    )
    with httpx.Client() as client:
        assert client.get("https://api.hh.ru/dontexist").status_code == 404


def test_type_response(httpx_mock: HTTPXMock):
    httpx_mock.add_response(
        method='GET',
        url='https://api.hh.ru/vacancies',
        status_code=200,
        match_headers={'Content-Type': 'application/json; charset=UTF-8'},
    )
    with httpx.Client() as client:
        response = client.get(
            'https://api.hh.ru/vacancies',
            headers={'Content-Type': 'application/json; charset=UTF-8'}
        )
