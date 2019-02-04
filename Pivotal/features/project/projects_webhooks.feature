@yellow
Feature: webhooks
  Background:
    Given I set up a "POST" request to "/projects" endpoint
    And I set up the data
      """
      {
      "name":"Executioner.dateTime"
      }
      """
    And I storage project how "project_1"
    And I send the request


  Scenario: Get webhooks
    Given I set up a "GET" request to "/projects/{:project_1:}/webhooks" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Post webhooks
    Given I set up a "POST" request to "/projects/{:project_1:}/webhooks" endpoint
    And I set up the data
      """
      {
      "webhook_url":"https://lapelicula.com",
      "webhook_version":"v5"
      }
      """
    When I send the request
    Then I get a "200" status code as response

  Scenario: Get webhooks with id
    Given I set up a "GET" request to "/projects/{:project_1:}/webhooks/234337" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Put webhooks with id
    Given I set up a "PUT" request to "/projects/{:project_1:}/webhooks/234337" endpoint
    And I set up the data
      """
      {
      "webhook_url":"https://mywebhooks2.com"
      }
      """
    When I send the request
    Then I get a "200" status code as response

  Scenario: Delete webhooks with id
    Given I set up a "DELETE" request to "/projects/{:project_1:}/webhooks/234337" endpoint
    When I send the request
    Then I get a "204" status code as response
