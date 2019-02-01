Feature: Get account

  Scenario: Get memberships
    Given I set up a "GET" request to "/projects/2242764/memberships" endpoint
    When I send the request
    Then I get a "200" status code as response


  Scenario: Get memberships with id
    Given I set up a "GET" request to "/projects/2242764/memberships/10006814" endpoint
    When I send the request
    Then I get a "200" status code as response

    