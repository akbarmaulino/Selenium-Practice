Feature: LoggedIn User View

  Scenario: Validate User is able to view after log in
    Given User Navigate to the Login page
    When User succesfully enters the log in details
    Then User should be able to view the product category page