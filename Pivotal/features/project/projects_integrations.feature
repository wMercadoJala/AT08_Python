Feature: Integrations

  Scenario: Get integrations with project_id
    Given I set up a "GET" request to "/projects/$PROJECT_ID/integrations" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Post integrations with project_id
    Given I set up a "POST" request to "/projects/$PROJECT_ID/integrations" endpoint
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


  Scenario: Get integrations with project_id and integration_id
    Given I set up a "GET" request to "/projects/$PROJECT_ID/integrations/$INTEGRATION_ID" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Post integrations with project_id and integration_id
    Given I set up a "POST" request to "/projects/$PROJECT_ID/integrations" endpoint
    And I set up the data
    """
    {
    "base_url":"http://some.th/ing",
    "name":"something"
    }
    """
    When I send the request
    Then I get a "200" status code as response

  Scenario: Delete integrations with project_id and integration_id
    Given I set up a "DELETE" request to "/projects/$PROJECT_ID/integrations/$INTEGRATION_ID" endpoint
    When I send the request
    Then I get a "200" status code as response


  Scenario: Get stories of integrations with project_id and integration_id
    Given I set up a "GET" request to "/projects/$PROJECT_ID/integrations/$INTEGRATION_ID/stories" endpoint
    When I send the request
    Then I get a "200" status code as response
