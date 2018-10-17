package DriverBase;

import java.io.File;
import java.io.IOException;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.By;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;

import util.Pro;

public class DriverBase {
public WebDriver driver;

public DriverBase(String browser) {
	SelectDriver selectdriver=new SelectDriver();
	this.driver=selectdriver.drivername(browser);
}
//关闭浏览器
public void stop() {
	System.out.println("stop webdriver");
	driver.close();
}
//窗口最大化
public void maxWindow() {
	driver.manage().window().maximize();
}
//鼠标移动
public void moveToElement(WebElement el) {
	Actions action=new Actions(driver);
	action.moveToElement(el);
}
//findElement 封装
public  WebElement findElement(String str) throws IOException {
	WebElement el=driver.findElement(bystr(str));
	return el;
}

public void getUrl(String url) {
	// TODO Auto-generated method stub
	driver.get(url);
}
public void click(WebElement e){
	e.click();
}
public  By bystr(String key1) throws IOException {
	  Pro prop=new Pro("src/main/java/conf/config.properties");
	  String key_value=prop.getPro(key1);
	  String key=key_value.split(">")[0];
	  String value=key_value.split(">")[1];
	  if(key.equals("id")) {
		  return By.id(value);
	  }
	  else if(key.equals("name")) {
		  return By.name(value);
	  }
	  else if(key.equals("class")) {
		  return By.className(value);
	  }
	  else {
		  return By.xpath(value);
	  }
}
public void jietu() {
	//获取当前系统的时间，并转换为字符串
	Long date=System.currentTimeMillis();
	String path=String.valueOf(date);
	//获取当前系统的路径
	String curPath =System.getProperty("user.dir");
	//图片的路径
	path=path+".png";
	String screenPaht="src/main/java/ScreenShot"+"/"+path;
	//获取图片
	File screen =((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
	try {
		//将获取的图片放到指定的路径中
		FileUtils.copyFile(screen,new File(screenPaht));
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
}

public void sendkeys(WebElement a,String b) throws IOException {
	a.sendKeys(b);
	}
//封装sendkeys
public void sendkeyss(WebElement a,String b) throws IOException {
	Pro prop=new Pro("src/main/java/config.properties");
	String sendKeys_value=prop.getPro(b);
	if(sendKeys_value!=null) {
	a.sendKeys(sendKeys_value);
	}
	else {
		System.out.println("配置文件未找到");
	}
}

}