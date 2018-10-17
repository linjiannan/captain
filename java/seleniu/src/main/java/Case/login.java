package Case;

import java.io.IOException;

import org.testng.annotations.Listeners;
import org.testng.annotations.Test;

import Business.loginPro;
import LinstenGetScreenShot.testListenTakeShot;
@Listeners({testListenTakeShot.class})
	public class login extends loginPro{
	public login() {
		super("chrome");
		// TODO Auto-generated constructor stub
	}

@Test
public void testlogin() throws IOException, InterruptedException{
	getUrl("https://www.imooc.com/");
	maxWindow();
	Thread.sleep(3);
	login();
}

}
