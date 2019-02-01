@smoke
Feature: Epics

  Scenario: Create a new epic
    Given I set up a "POST" request to "/projects/2242582/epics" endpoint
    And I set up the header
    """
    {
      "Content-Type": "application/json"
    }
    """
    And I set up the data
    """
    {
      "name":"Tractor Beams"
    }
    """
    When I send the request
    Then I get a "200" status code as response

  Scenario: Get an specified project
    Given I set up a "GET" request to "/projects/2242582/epics" endpoint
    When I send the request
    Then I get a "200" status code as response
