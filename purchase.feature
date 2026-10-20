@smoke @regression @purchase
Feature: End-to-End Purchase Journey

  As a standard customer
  I want to purchase a product successfully
  So that I can verify the complete shopping journey

  Scenario: Successfully purchase a Sauce Labs Backpack
    Given I am logged in as a standard user
    Then the Products page should be displayed
    When I add "Sauce Labs Backpack" to the cart
    Then the cart badge should display "1"
    When I open the shopping cart
    Then the cart should contain "Sauce Labs Backpack"
    When I proceed to checkout
    And I enter valid customer details
    And I continue to the order overview
    Then the order overview should display "Sauce Labs Backpack"
    When I finish the purchase
    Then the order confirmation page should be displayed
    And the confirmation message should be "Thank you for your order!"