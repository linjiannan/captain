package ExtentReporter;

import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestResult;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;

public class ExtentTestNGITestListener implements ITestListener {

    private static ExtentReports extent = ExtentManager.createInstance("extent66.html");
    //private static ThreadLocal parentTest = new ThreadLocal();
    //private static ThreadLocal test = new ThreadLocal();
    //不造为嘛，代码苦手表示用上面的代码就是编译报错，所以就随便改了改，如下，就通过了。。
    private static ThreadLocal<ExtentTest> parentTest = new ThreadLocal();
    private static ThreadLocal<ExtentTest> test = new ThreadLocal();

    public synchronized void onStart(ITestContext context) {
        ExtentTest parent = extent.createTest(getClass().getName());
        parentTest.set(parent);
    }

    public synchronized void onFinish(ITestContext context) {
        extent.flush();
    }

    public synchronized void onTestStart(ITestResult result) {
        ExtentTest child = parentTest.get().createNode(result.getMethod().getMethodName());
        test.set(child);
    }

    public synchronized void onTestSuccess(ITestResult result) {
        test.get().pass("Test passed");
    }

    public synchronized void onTestFailure(ITestResult result) {
        test.get().fail(result.getThrowable());
    }

    public synchronized void onTestSkipped(ITestResult result) {
        test.get().skip(result.getThrowable());
    }

    public synchronized void onTestFailedButWithinSuccessPercentage(ITestResult result) {

    }
}

