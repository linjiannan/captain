package jacoco.jacoco_demo;

import org.junit.Assert;
import org.junit.Test;
//链接：https://www.cnblogs.com/fnng/p/7923314.html
//https://my.oschina.net/wangmengjun/blog/974067
public class Calculator_Test {

	private Calculator instance = new Calculator();

	@Test
	public void testAdd() {
		int a = 10;
		int b = 20;
		int expected = 30;
		Assert.assertEquals(expected, instance.add(a, b));
	}

	@Test
	public void testSub() {
		int a = 10;
		int b = 20;
		int expected = -10;
		Assert.assertEquals(expected, instance.sub(a, b));
	}
}