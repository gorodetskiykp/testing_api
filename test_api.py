from http import HTTPStatus
import pytest
import requests
from pprint import pprint
from requests.models import Response



ENDPOINT = 'https://api.hh.ru/vacancies/?searched=python'
ENDPOINT_ERROR = 'https://api.hh.ru/search/vacancy?text=Python&from=suggest_post&area=2081&hhtmFrom=main&hhtmFromLabel=vacancy_search_line'


class NotListException(Exception):
    pass


# def test_api_get_wrong_endpoint():
#     resp = requests.get(ENDPOINT_ERROR)
#     assert verify_404_body(resp)

def test_api_get_wrong_endpoint_return_not_tuple():
    resp = requests.get(ENDPOINT_ERROR)
    with pytest.raises(NotListException):
        verify_404_body(resp)

    # try:
    #     verify_404_body(resp)
    # except NotListException:
    #     assert True


def verify_404_body(resp: Response) -> bool:
    if resp.status_code != HTTPStatus.NOT_FOUND:
        return False

    if resp.status_code != HTTPStatus.NOT_FOUND:
        return False

    resp = resp.json()
    if set(resp.keys()) != {"errors", "request_id"}:
        return False
    if 'errors' not in resp:
        return False
    assert 'request_id' in resp
    assert len(resp["errors"]) == 1
    if type(resp["errors"]) != tuple:
        raise NotListException
    assert "type" in resp["errors"][0]
    assert resp["errors"][0]["type"] == "not_found"
    return True
