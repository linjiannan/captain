package util;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class Pro {
private Properties prope;
private String path;

public  Pro(String lujing) throws IOException {
	this.path=lujing;
	this.prope=readPro();
}
	
public Properties readPro() throws IOException {
	//"src/config.properties"
	Properties prop=new Properties();
	InputStream ips= new FileInputStream(path);
    prop.load(ips);
    return prop;
}
public String getPro(String key) {
	if(prope.containsKey(key)) {
	String key_value=prope.getProperty(key);
	return key_value;
	}
	else {
		System.out.println("配置文件没有你要的key值");
		return "";
	}
}
}
