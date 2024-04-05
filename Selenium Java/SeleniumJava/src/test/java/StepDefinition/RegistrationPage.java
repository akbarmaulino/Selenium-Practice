package StepDefinition;
import io.cucumber.java.en.Then;
import static org.junit.Assert.assertEquals;

import static pages.ProductCategoryPage.*;

public class RegistrationPage {

    @Then("^User should be able to view the Registration page$")
    public void user_should_be_able_to_view_registration_page(){
        String actualProductCategory = visiblity_productCategory();
        assertEquals(actualProductCategory, "User Registration Page");

    }
}