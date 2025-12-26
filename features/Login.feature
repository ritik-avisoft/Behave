Feature: Login
    @correct-login
    Scenario Outline:verify user login
        Given I am on the login page
        When "<user_id>" user enter correct login credentials
        Then User should be on product page
        Examples:
            |user_id     |
            |standard    | 
            |problem     | 
            |performance |

    @invalid-login
    Scenario: verify login with blank credentials
        Given I am on the login page
        When I keep username and password blank
        Then User should see error message for blank credentials

    @invalid-username
    Scenario: verify login with blank username
        Given I am on the login page  
        When I keep blank username and fill valid password
        Then User should see error message for blank username

    @invalid-password 
    Scenario: verify login with invalid password
        Given I am on the login page
        When I filled valid username and invalid password
        Then User should see error message for invalid credentials

    @locked-out
    Scenario:verify locked out user login
        Given I am on the login page
        When If "locked" user enter correct login credentials
        Then User should see a locked out error message