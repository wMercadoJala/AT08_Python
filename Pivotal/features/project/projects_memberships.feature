Feature: Get account

  Scenario: Post memberships with project_id
    Given I set up a "POST" request to "/projects/$PROJECT_ID/memberships" endpoint
    And I set up the data
    """
    {
    "person_id":106,
    "role":"member"
    }
    """
    When I send the request
    Then I get a "200" status code as response

  Scenario: Post memberships with person_id
    Given I set up a "POST" request to "/projects/$PERSON_ID/memberships" endpoint
    And I set up the data
    """
    {
    "person_id":106,
    "role":"member"
    }
    """
    When I send the request
    Then I get a "200" status code as response

  Scenario: Get memberships to name
    Given I set up a "POST" request to "/projects/$NAME/memberships" endpoint
    And I set up the data
    """
    {
    "person_id":106,
    "role":"member"
    }
    """
    When I send the request
    Then I get a "200" status code as response

  Scenario: Get memberships with project_id
    Given I set up a "GET" request to "/projects/$PROJECT_ID/memberships" endpoint
    When I send the request
    Then I get a "200" status code as response


  Scenario: Get memberships with project_id and membership_id
    Given I set up a "GET" request to "/projects/$PROJECT_ID/memberships/$MEMBERSHIP_ID" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Delete memberships with project_id and membership_id
    Given I set up a "DELETE" request to "/projects/$PROJECT_ID/memberships/$MEMBERSHIP_ID" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Put memberships with project_id and membership_id
    Given I set up a "PUT" request to "/projects/$PROJECT_ID/memberships/$MEMBERSHIP_ID" endpoint
    And I set up the data
    """
    {
    "role":"viewer"
    }
    """
    When I send the request
    Then I get a "200" status code as response
