Feature: Get account

  Scenario: Get Account
    Given I set up a "GET" request to "/accounts/1081141" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Get accounts where user is owner or admin
    Given I set up a "GET" request to "/accounts" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Get account summaries
    Given I set up a "GET" request to "/account_summaries?with_permission=project_creation" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Get memberships of an account
    Given I set up a "GET" request to "/accounts/1081146/memberships" endpoint
    When I send the request
    Then I get a "200" status code as response


