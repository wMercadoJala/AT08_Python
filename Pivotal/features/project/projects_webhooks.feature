@smoke
Feature: webhooks

  Background:
    Given I set up a "POST" request to "/pŕojects" endpoint
    And I set up the data
      """
      {
      "name":"my first project"
      }
      """
    And I send the request

  Scenario: Get webhooks
    Given I set up a "GET" request to "/projects" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Post webhooks
    Given I set up a "POST" request to "/projects/2244435/webhooks" endpoint
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
    Given I set up a "GET" request to "/projects/2244435/webhooks/234428" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Put webhooks with id
    Given I set up a "PUT" request to "/projects/2244435/webhooks/234428" endpoint
    And I set up the data
      """
      {
      "webhook_url":"https://mywebhooks2.com"
      }
      """
    When I send the request
    Then I get a "200" status code as response

  Scenario: Delete webhooks with id
    Given I set up a "DELETE" request to "/projects/2244435/webhooks/234427" endpoint
    When I send the request
    Then I get a "204" status code as response
