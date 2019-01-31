Feature: Get account

  Scenario: Get Account
    Given I set up a "GET" request to "/accounts/1081108" endpoint
    When I send the request
    Then I get a "200" status code as response
