
Feature: Authentication

  @Login
 	Scenario Outline:  User Login without input any credential
    Given The User Already in The Youtube Music Login Page
    When The User Not Fill <Email> to Login
    Then The User can see error message that Email Or Password must be fill

	Examples: 
	| Email |
	|  |