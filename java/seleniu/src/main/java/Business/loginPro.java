package Business;

import java.io.IOException;
import Handle.loginHandle;
public class loginPro extends loginHandle{

	public loginPro(String browser) {
		super(browser);
		// TODO Auto-generated constructor stub
	}

	public void login() throws IOException, InterruptedException{
		click_loginButton();
		Thread.sleep(2000);//https://www.cnblogs.com/klmei/p/7065592.html
		sendkeys_username();
		sendkeys_password();
	}

}
