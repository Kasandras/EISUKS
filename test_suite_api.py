import requests


class TestSuite:

    @classmethod
    def setup_class(cls):
        cls.session = requests.session()

    def test_auth(self):

        url = 'http://gossluzhba1.qtestweb.office.quarta-vk.ru/#/login'

        r = self.session.get(url=url, auth=('AndRyb', '123123/'))
        assert r.text == ""

    def test_create_new_user(self):

        url = 'http://gossluzhba1.qtestweb.office.quarta-vk.ru/api/personalfile/personaldata/create'

        payload = {'lastName': "Сулаев",
                   'firstName': "Сидор",
                   'middleName': "Сидорович",
                   'birthDate': "12.02.1988",
                   'insuranceCertificateNumber': "11546175141"}

        r = self.session.post(url=url, data=payload, auth=('1', '123123/'))
        print(r.text)

    def test_