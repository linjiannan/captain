package Case;

import java.io.IOException;

import org.testng.Reporter;
import org.testng.annotations.Listeners;
import org.testng.annotations.Test;
import org.testng.log4testng.Logger;

import Business.loginPro;
import LinstenGetScreenShot.testListenTakeShot;
import util.Log;
@Listeners({testListenTakeShot.class})
public class login extends loginPro{
	public login() {
		super("chrome");
		// TODO Auto-generated constructor stub
	}

@Test
public void testlogin() throws IOException, InterruptedException{
	Reporter.log("login case开始");
	//getUrl("https://www.imooc.com/");
	//maxWindow();
	Thread.sleep(3);
	Reporter.log("窗口最大化后延时3秒");
    Log.info("aaaaaa");
    Log.debug("aaaaaa");
    Log.error("aaaaaa");
    
	
	
}


}
