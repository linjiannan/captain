package DriverBase;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.ie.InternetExplorerDriver;
import org.openqa.selenium.remote.DesiredCapabilities;

public class SelectDriver {
public WebDriver drivername(String browser) {
	if(browser.equalsIgnoreCase("firefox")) {
		System.setProperty("webdriver.firefox.bin", "E:\\firefox\\firefox.exe");
		WebDriver driver=new FirefoxDriver();
		return driver;
	}
	else if(browser.equalsIgnoreCase("chrome")) {
		DesiredCapabilities sCaps = new DesiredCapabilities();
		sCaps.setJavascriptEnabled(true);
		System.setProperty("webdriver.chrome.driver","E:\\chrome\\chromedriver.exe");
		WebDriver driver=new ChromeDriver();
		return driver;
	}
	else {
		 System.setProperty("webdriver.ie.driver","E:\\Iedriver\\IEDriverServer_X64\\IEDriverServer.exe");
		 WebDriver driver=new InternetExplorerDriver();
		 return driver;
	}
}
}
