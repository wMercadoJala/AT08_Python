Feature: Add a member to an account adn delete it
  
#  Scenario: Add a member to an account
#    Given I set up a "POST" request to "/accounts/1080889/memberships" endpoint
#    And I set up the header
#      | Name header   | Content header    |
#      | Content-Type  | application/json  |
#    And I set up the data
#      """
#      {
#      "person_id": 3143926
#      }
#      """
#    When I send the request
#    Then I get a "200" status code as response
  
  Scenario: Delete a member from an account
    Given I set up a "DELETE" request to "/accounts/1080889/memberships/3143926" endpoint
#    And I set up the header
#      | Name header   | Content header    |
#      | Content-Type  | application/json  |
    When I send the request
    Then I get a "200" status code as response
