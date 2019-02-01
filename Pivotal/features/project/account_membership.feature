@smoke
Feature: Account Memberships

  Scenario: List all of the memberships in an account.
    Given I set up a "GET" request to "/accounts/{account_id}/memberships" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Create a new membership in an account by email.
    Given I set up a "POST" request to "/accounts/1081260/memberships" endpoint
    And I set up the data
      """
      {
      "email":"machine123@mailinator.com",
      "initials":"machine123",
      "name":"MA"
      }
      """
    When I send the request
    Then I get a "200" status code as response

  Scenario: Create a new membership in an account by ID
    Given I set up a "POST" request to "/accounts/1081260/memberships" endpoint
    And I set up the data
      """
      {
      "person_id":108
      }
      """
    When I send the request
    Then I get a "200" status code as response

   Scenario: Get an individual account membership, requested by the person_id.
    Given I set up a "GET" request to "/accounts/1081260/memberships/3143789" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Updates the specified account membership.
    Given I set up a "PUT" request to "/accounts/1081260/memberships/3143789" endpoint
    And I set up the data
      """
      {
      "project_creator":true
      }
      """
      When I send the request
      Then I get a "200" status code as response

   Scenario: Delete the specified account membership.
    Given I set up a "DELETE" request to "/accounts/1081260/memberships/3143789" endpoint
      When I send the request
      Then I get a "204" status code as response
