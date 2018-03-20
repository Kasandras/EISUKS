import requests
import pytest
import json


class TestSuite:

    structure_id = ""

    @classmethod
    def setup_class(cls):
        cls.session = requests.session()

    def is_user_logged(self):

        url = "http://gossluzhba1.qtestweb.office.quarta-vk.ru/Dashboard/Hr"

        request = requests.session().get(url=url)

    def test_auth(self):

        url = 'http://gossluzhba1.qtestweb.office.quarta-vk.ru/#/login'

        r = self.session.get(url=url, auth=('AndRyb', '123123/'))
        print(r.text)

    def t1est_create_new_user(self):

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

        r = self.session.post(url=url, data=payload, auth=('AndRyb', '123123/'))
        print(r.text)
        # .{"id":"14efff40-eb51-46e4-be89-a84e0a116247"}

    def tes1t_create_structure(self):

        url = "http://gossluzhba1.qtestweb.office.quarta-vk.ru/api/staff/project/save"

        payload = {"name":"Тестирование введения в действие2",
                   "staffLimit":0,
                   "organization":{"id":"dd377bcd-4337-4871-8b4a-7ba9fbabf957",
                                   "name":"Automation",
                                   "hierarchyPath":"/168/",
                                   "type":"UrbanDistrict",
                                   "subType":None,
                                   "parentId":"6b600191-8099-4370-b7bf-7508956ed375",
                                   "useStaffStructure":False},
                   "organizationId":"dd377bcd-4337-4871-8b4a-7ba9fbabf957"}

        r = self.session.post(url=url, data=payload, auth=('AndRyb', '123123/'))
        TestSuite.structure_id = json.loads(r.text)["id"]
        print(TestSuite.structure_id)

    def te1st_create_subdivision(self):

        url = "http://gossluzhba1.qtestweb.office.quarta-vk.ru/api/staff/department/save"

        payload = {"renames": [],
                   "subType": {"id": 2, "name": "Структурное подразделение"},
                   "name": "Новое подразделение",
                   "projectId": "2d30d746-c135-420a-8746-782ba9f2dc54",
                   "projectName": "New project2",
                   "organizationId": "dd377bcd-4337-4871-8b4a-7ba9fbabf957",
                   "organizationName": "Automation",
                   "stateId": "efddab89-1402-4d1d-aeab-98d7fb045dd2",
                   "nameGenitive": "2",
                   "nameDative": "3",
                   "nameAccusative": "4",
                   "assignedPosts": [],
                   "selectedPostsCount": 1,
                   "isNew": True
        }

        r = self.session.post(url=url, data=payload, auth=('AndRyb', '123123/'))
        print(r.text)

    def test_make_active_structure(self):
        url = "http://gossluzhba1.qtestweb.office.quarta-vk.ru/api/staff/project/save"

        payload = {"id":"5c0d43e9-b8aa-4c32-a062-9cdd3476c185","name":"Новый проект","state":None,"regularStaffing":0,"substitutedStaffing":0,"subunitCount":0,"staffLimit":0,"organizationId":"dd377bcd-4337-4871-8b4a-7ba9fbabf957","organizationName":"Automation","orderDate":"22.01.2018","orderNumber":"14444","isProject":True,"isActive":False,"isArchive":False,"releaseDate":"22.01.2018","payroll":0}

        r = self.session.put(url=url, data=payload, auth=('AndRyb', '123123/'))
        print(r.text)

    def te1st_update_profile(self):

        url = 'http://gossluzhba1.qtestweb.office.quarta-vk.ru/api/personalfile/commoninformation/save'

        payload = {
            'birthDate': "02.12.1988",
            'firstName': "Иван",
            'id': "14efff40-eb51-46e4-be89-a84e0a116247",
            'lastName': "Иванов",
            'insuranceCertificateNumber': "11547175247",
            'wasConvicted': False,
            'gender': {
                'code': "1",
                'id': "b8ddbfee-2456-4919-abcf-1091031e03b1",
                'name': "Мужской",
                'positionInList': 0,
                'singularName': None
            },
            'middleName': "Иванович"
        }

        r = self.session.post(url=url, data=payload, auth=('AndRyb', '123123/'))
        print(r.text)
