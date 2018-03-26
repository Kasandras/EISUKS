import requests
import pytest
import json

structure_id = ""
session = requests.session()


def is_user_logged(self):

    url = "http://gossluzhba1.qtestweb.office.quarta-vk.ru/Dashboard/Hr"

    request = requests.session().get(url=url)


def test_auth():

    url = 'http://gossluzhba1.qtestweb.office.quarta-vk.ru/#/login'

    r = session.get(url=url, auth=('AndRyb', '123123/'))
    print(r.text)


def add_vacancy():

    url = 'http://gossluzhba1.qtestweb.office.quarta-vk.ru/api/personalfile/personaldata/create'

    payload = {'lastName': "Testing",
               'firstName': "Test",
               'middleName': "Testing",
               'gender': {
                    'code': "1",
                    'id': "b8ddbfee-2456-4919-abcf-1091031e03b1",
                    'name': "Мужской",
                    'positionInList': 0,
                    'singularName': None
               },
               'birthDate': "12.02.1988",
               'insuranceCertificateNumber': "11546175242"}

    r = session.post(url=url, data=payload, auth=('AndRyb', '123123/'))
    print(r.text)
