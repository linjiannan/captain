package conf;

import java.io.File;

public class one {
	public static void main(String args[]){
		File directory = new File("");//设定为当前文件夹 
		String curPath =System.getProperty("user.dir");
		System.out.print(curPath);
		System.out.println(directory.getAbsolutePath());
	}
	
}
