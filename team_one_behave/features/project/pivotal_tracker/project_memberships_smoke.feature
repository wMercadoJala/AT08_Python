@smoke
Feature: Get Project Memberships

  Scenario: Get Project Memberships
    Given I set up a "GET" request to "/projects/2242689/memberships" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Post an specified project integration
    Given I set up a "POST" request to "/projects/2242689/memberships" endpoint
    And I set up the data
    """
    {
      "person_id": 3143926,
      "role": "member"
    }
    """
    When I send the request
    Then I get a "200" status code as response