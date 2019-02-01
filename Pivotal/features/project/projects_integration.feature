Feature: Operations on a project's integrations.
  Scenario: Returns a projects's integrations.
    Given I set up a "GET" request to "/projects/2242764/integrations" endpoint
    When I send the request
    Then I get status code "200"
