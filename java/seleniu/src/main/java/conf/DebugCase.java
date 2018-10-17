package conf;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;


public class DebugCase {
  public static WebDriver driver;
  public void InitDriver() {
	System.setProperty("webdriver.chrome.driver","E:\\chrome\\chromedriver.exe");
	driver=new ChromeDriver();
  }
  public static void main(String args[]) throws InterruptedException {
	  DebugCase test=new DebugCase();
	  test.InitDriver();
      driver.get("http://www.imooc.com/");
	  driver.manage().window().maximize();
	  WebElement loginbutton=driver.findElement(By.id("js-signin-btn"));
	  if(loginbutton.isDisplayed()){
		  System.out.println("true");
	  }
	  loginbutton.click();
	  Thread.sleep(3000);
	  driver.findElement(By.name("email")).sendKeys("1186535553");
  }
  }
