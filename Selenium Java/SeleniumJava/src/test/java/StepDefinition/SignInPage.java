package StepDefinition;

import io.cucumber.java.en.When;

import static pages.SignInPage.*;

public class SignInPage {

    @When("^User succesfully enters the log in details$")
    public void user_logsin_to_login_page(){
        sendkeys_username();
        sendkeys_password();
        click_login_btn();
    }
}
