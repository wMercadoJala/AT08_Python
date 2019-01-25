Feature: Thes feature
  Scenario Outline: My first test
    Given I am a student
    When I learn "<amount>" test
    Then I can work in jala

    Examples:
      | amount  |
      | 1  |
      | 2  |