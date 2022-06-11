Feature: As a user, I can check hi dollars changes within 7 days
  Scenario: Check dollars changes within 7 days
    Given I am on CoinMarketCap homepage
    When I am on Static page
    Then I search hi coin with search bar
    Then I navigate to hi dollars info page
    Then I check hi dollars changes within 7 days