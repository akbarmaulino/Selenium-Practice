package StepDefinition;

import io.cucumber.java.en.Given;
import static pages.HomePage.*;
public class BasePage {

    @Given("^User Navigate to the Login page$")
    public void user_navigate_to_the_Login_page() throws Throwable{
        click_hamburger_menu();
        click_signIn_Link();
    }

}
