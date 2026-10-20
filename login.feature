Feature: SauceDemo login

  @smoke
  Scenario: Invalid login shows an error
    Given I open the SauceDemo login page
    When I log in with invalid credentials
    Then I should see an authentication error
    And I should remain on the login page