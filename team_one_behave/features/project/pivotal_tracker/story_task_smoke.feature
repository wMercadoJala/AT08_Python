Feature: Get the tasks of an specific story of an specific project.

  Scenario: Get tasks of an story
    Given I set up a "GET" request to "/projects/2243551/stories/163686235/tasks" endpoint
    When I send the request
    Then I get a "200" status code as response

  Scenario: Return a task created
    Given I set up a "POST" request to "/projects/2243551/stories/163686235/tasks" endpoint
    And I set up the data
    """
      {
      "description": "Task created in PyCharm"
      }
    """
    When I send the request
    Then I get a "200" status code as response

  Scenario: Return an specific task
    Given I set up a "GET" request to "/projects/2243551/stories/163686235/tasks/64806099?fields=description%2Ccomplete" endpoint
    When I set up the data
    """
      {
      "description": "Story task."
      }
    """
    When I send the request
    Then I get a "200" status code as response
    