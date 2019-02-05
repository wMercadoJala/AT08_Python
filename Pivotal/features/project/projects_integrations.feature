@smoke @create_project
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
    "base_url":"https://elrincondejiraversion.atlassian.net",
    "name":"algointeresante2",
    "type":"other"
    }
    """
    When I send the request
    Then I get a "200" status code as response

  @create_integration
  Scenario: Get integrations with project_id and integration_id
    Given I set up a "GET" request to "/projects/$PROJECT_ID/integrations/$INTEGRATION_ID" endpoint
    When I send the request
    Then I get a "200" status code as response

  @create_integration
  Scenario: Delete integrations with project_id and integration_id
    Given I set up a "DELETE" request to "/projects/$PROJECT_ID/integrations/$INTEGRATION_ID" endpoint
    When I send the request
    Then I get a "204" status code as response

  @create_integration
  Scenario: Put integrations with project_id and integration_id
    Given I set up a "PUT" request to "/projects/$PROJECT_ID/integrations/$INTEGRATION_ID" endpoint
    And I set up the data
    """
    {
    "base_url":"https://elrincondejiraoculto.atlassian.net",
    "name":"rinconcito"
    }
    """
    When I send the request
    Then I get a "200" status code as response
    
