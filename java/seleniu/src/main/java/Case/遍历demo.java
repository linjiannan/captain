package Case;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebElement;
import org.testng.Reporter;
import org.testng.annotations.Listeners;
import org.testng.annotations.Test;
import org.testng.log4testng.Logger;

import Business.loginPro;
import DriverBase.DriverBase;
import LinstenGetScreenShot.testListenTakeShot;
import util.Log;
@Listeners({testListenTakeShot.class})
public class 遍历demo extends loginPro{
	public 遍历demo() {
		super("chrome");
		// TODO Auto-generated constructor stub
	}

public void testlogin() throws IOException, InterruptedException{
	//Reporter.log("login case开始");
	getUrl("https://coding.imooc.com/");
	//((JavascriptExecutor) driver).executeScript("window.scrollTo(0,document.body.scrollHeight)");
}
@Test
public void CourseList(){
	getUrl("https://coding.imooc.com/");
	List<String> listString = this.listElement();
	for(int i=0;i<listString.size();i++){
		System.out.println(listString.get(i));
		if(driver.findElement(By.xpath("//*[contains(text(),'"+listString.get(i)+"')]"))!=null){
			WebElement element=driver.findElement(By.xpath("//*[contains(text(),'"+listString.get(i)+"')]"));
			//下面两句是滚动条切换到元素的位置
			String script = "return arguments[0].scrollIntoView();";
			((JavascriptExecutor) driver).executeScript(script, element);
			element.click();
			back();
			}
		}
}

//获取所有课程的list
public List<String>  listElement(){ //
	List<String> listString=new ArrayList<String>();
	WebElement element=driver.findElement(By.className("shizhan-course-list"));
	List<WebElement> listElement=element.findElements(By.className("shizhan-course-box"));
	for(WebElement el:listElement){
		//切割空格是因为text的定位跟class一样，有空格是定位不到的
		listString.add((el.findElement(By.className("shizan-desc")).getText().split(" ")[0]));
	}
	return listString;
	
}
}
