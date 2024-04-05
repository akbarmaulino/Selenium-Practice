package steps;

import io.cucumber.java.en.Given;
import io.cucumber.java.en.Then;
import io.cucumber.java.en.When;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class HomeStepsDefinition {

    public static WebDriver driver;
    @Given("I navigate to the homepage")
    public void i_navigate_to_the_homepage() {
        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        System.setProperty("webdriver.chrome.driver", "D:\\Aplikasi Donwload\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe");
        driver = new ChromeDriver(options);
        driver.get("https://www.facebook.com/");
    }
    @When("Navigate Forgot password link")
    public void navigate_forgot_password_link() {
        driver.findElement(By.xpath("//a[text()='Forgotten password?']")).click();
    }
    @Then("I should see forgot password page")
    public void i_should_see_forgot_password_page() {
        driver.findElement(By.xpath("//h2 [text()='Find Your Account']")).isDisplayed();


    }
}
