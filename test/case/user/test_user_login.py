from test.case.BaseCase import BaseCase

class TestUserLogin(BaseCase):
    def test_login_success(self):
        case_data=self.get_case_data("login_ok")
        self.send_request(case_data)
    def test_login_fail1(self):
        case_data=self.get_case_data("login_err1")
        self.send_request(case_data)
