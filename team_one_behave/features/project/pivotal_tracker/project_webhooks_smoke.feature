@smoke
Feature: Get Project Webhooks

  Scenario: Get Project Webhooks
    Given I set up a "GET" request to "/projects/2242689/webhooks" endpoint
    When I send the request
    Then I get a "200" status code as response

