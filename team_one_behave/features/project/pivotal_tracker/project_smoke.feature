@smoke
Feature: Project

  Scenario: Get an specified project
    Given I set up a "GET" request to "/projects/2242582" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Put an specified project
    Given I set up a "PUT" request to "/projects/2242582" endpoint
    And I set up the data
    """
    {
      "name": "Project"
    }
    """
    When I send the request
    Then I get a "200" status code as response

  Scenario: Delete an specified project
    Given I set up a "DELETE" request to "/projects/2242779" endpoint
    When I send the request
    Then I get a "204" status code as response

