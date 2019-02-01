@smoke
Feature: Project Integration

  Scenario: Get an specified project integration
    Given I set up a "GET" request to "/projects/2242582/integrations" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Post an specified project integration
    Given I set up a "POST" request to "/projects/2242582/integrations" endpoint
    And I set up the data
    """
    {
      "active":false,
      "base_url":"http://some.th/ing",
      "name":"something",
      "type":"other"
    }
    """
    When I send the request
    Then I get a "200" status code as response
