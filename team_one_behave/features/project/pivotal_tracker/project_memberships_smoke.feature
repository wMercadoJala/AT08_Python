@smoke
Feature: Get Project Memberships

  Scenario: Get Project Memberships
    Given I set up a "GET" request to "/projects/2242689/memberships" endpoint
    When I send the request
    Then I get a "200" status code as response
