Feature: Get Projects

  Scenario: Get Projects
    Given I set up a "GET" request to "/projects" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Get Projects Webhooks
    Given I set up a "GET" request to "/projects/2242689/webhooks" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Get Projects Memberships
    Given I set up a "GET" request to "/projects/2242689/memberships" endpoint
    When I send the request
    Then I get a "200" status code as response
