from page.loginPage import loginPage
class loginHandle:
    def __init__(self,i):
        self.loginPage = loginPage(i)
        print("loginPage 的i：" + str(i))

    def inputUsername(self,username):
        self.loginPage.get_login_username().send_keys(username)
    def inputPassword(self,password):
        self.loginPage.get_login_password().send_keys(password)
    def clickLoginButton(self):
        self.loginPage.get_loginButton().click()
    def get_fail_toast(self,message):
        element=self.loginPage.get_tost_element(message)
        if element:
            return True
        else:
            return False