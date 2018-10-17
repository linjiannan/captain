package LinstenGetScreenShot;

import org.testng.ITestResult;
import org.testng.TestListenerAdapter;

import Case.login;

public class testListenTakeShot extends TestListenerAdapter{
	
@Override
public void onTestSuccess(ITestResult tr) {
	super.onTestSuccess(tr);
}
@Override
public void onTestFailure(ITestResult tr) {
	super.onTestFailure(tr);
	testListenTakeShot(tr);
}
@Override
public void onTestSkipped(ITestResult tr) {
	super.onTestSkipped(tr);
	
}
public void testListenTakeShot(ITestResult tr) {
  login b=(login)tr.getInstance();
  b.jietu();
}
}

