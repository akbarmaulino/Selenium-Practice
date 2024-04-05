package pages;
import org.openqa.selenium.By;

import utility.BrowserDriver;

public class RegistationPage extends BrowserDriver {

    public static String registration_heading_xpath = "/html/body/center/h1";


    public static String visibility_registrationheading() throws InterruptedException {
        Thread.sleep(2000);
        String getRegistration = driver.findElement(By.xpath("registration_heading_xpath")).getText();
        return getRegistration;
    }
}




