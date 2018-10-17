package Case;

import java.io.IOException;

import org.testng.Reporter;
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
	Reporter.log("login case开始");
	getUrl("https://www.imooc.com/");
	maxWindow();
	Reporter.log("窗口最大化后延时3秒");
	Thread.sleep(3);
	login();
}

}
