@smoke
Feature: Get Project Webhooks

  Scenario: Get Project Webhooks
    Given I set up a "GET" request to "/projects/2242689/webhooks" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Post an specified project integration
    Given I set up a "POST" request to "/projects/2242689/webhooks" endpoint
    And I set up the data
    """
    {
      "webhook_url":"https://www.pivotaltracker.com",
      "webhook_version":"v5"
    }
    """
    When I send the request
    Then I get a "200" status code as response