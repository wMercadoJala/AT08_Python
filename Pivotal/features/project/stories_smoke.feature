@smoke2
Feature: Get stories
  Scenario: Get All stories
    Given I set up a "GET" request to "/projects/$PROJECT_ID/stories?date_format=millis&with_state=unstarted" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Post new stories
    Given I set up a "POST" request to "/projects/$PROJECT_ID/stories" endpoint
    And I set up the data
      """
      {
      "name":"Storie1 created by team2"
      }
      """
    When I send the request
    Then I get a "200" status code as response
    
