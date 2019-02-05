Feature: Get account

  Scenario: Get memberships
    Given I set up a "GET" request to "/projects/2242764/integrations" endpoint
    When I send the request
    Then I get a "200" status code as response


  Scenario: Get memberships with id
    Given I set up a "GET" request to "/projects/2242764/integrations/48948" endpoint
    When I send the request
    Then I get a "200" status code as response

    