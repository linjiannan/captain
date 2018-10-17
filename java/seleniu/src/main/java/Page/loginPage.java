package Page;

import java.io.IOException;

import org.openqa.selenium.WebElement;

import DriverBase.DriverBase;

public class loginPage extends DriverBase {
	public loginPage(String browser) {
		super(browser);
		// TODO Auto-generated constructor stub
	}
	public WebElement login_button() throws IOException{
		return findElement("loginbutton");
	}
   public WebElement username() throws IOException{
	   return findElement("username");
   }
   public WebElement password() throws IOException {
	   return findElement("password");
   }

}
