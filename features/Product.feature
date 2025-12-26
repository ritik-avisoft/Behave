Feature: Product page

    Background: 
        Given I am on the login page
        When "standard" user enter correct login credentials
        Then User should be on product page

    @product_test
    Scenario: Product listing verification
        Given I am on the product page
        Then User should see all products displayed
        And Each product should have an image
        And Each product should have a title
        And Each product should have a price
        And Each product should have an "Add to cart" button

    Scenario: Product sorting functionality
        Given User is on the product page
        When User clicks on sort dropdown
        Then User should see following sort options
            | Name (A to Z)         |
            | Name (Z to A)         |
            | Price (low to high)   |
            | Price (high to low)   |
        When User selects a sort option
        Then Products should be sorted accordingly

    Scenario: Product details verification
        Given User is on the product page
        When User clicks on a product
        Then User should see detailed product information
        And User should see product description
        And User should see product price
        And User should see "Add to cart" button

