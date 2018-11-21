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
public int width;
public int heigth;

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
//封装
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
	  else if(key.equals("className")) {
		  return By.className(value);
	  }
	  else if(key.equals("tagName")){
		  return By.tagName(value);
	  }
	  else if(key.equals("linkTest")){
		  return By.linkText(value);
	  }
	  else if(key.equals("partialLinkText")){
		  return By.partialLinkText(value);  
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
//获取当前屏幕的大小
public void test(){
	width=driver.manage().window().getSize().width;
	heigth=driver.manage().window().getSize().height;
}
//刷新网页
public void refresh(){
	driver.navigate().refresh();
}
//前进到前一步操作
public void forward(){
	driver.navigate().forward();
}
//后退到上一步操作
public void back(){
	driver.navigate().back();
}
//关闭窗口
public void quit(){
	driver.quit();
}
public String getAttribute(WebElement el,String value){
	return el.getAttribute(value);
}
public String getText(WebElement el){
	return el.getText();
}
}