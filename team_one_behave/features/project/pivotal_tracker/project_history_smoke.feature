@smoke
Feature: Project History

  Scenario: Get an specified project history
    Given I set up a "GET" request to "/projects/2242582/history/days" endpoint
    When I send the request
    Then I get a "200" status code as response
