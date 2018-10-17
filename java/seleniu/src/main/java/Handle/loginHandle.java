package Handle;

import java.io.IOException;

import Page.loginPage;

public class loginHandle extends loginPage{

public loginHandle(String browser) {
		super(browser);
		// TODO Auto-generated constructor stub
	}
public void click_loginButton() throws IOException{
	 click(login_button());
}
public void sendkeys_username() throws IOException{
      sendkeys(username(),"111111");
}
public void sendkeys_password() throws IOException{
	sendkeys(password(),"1222122");
}

}
