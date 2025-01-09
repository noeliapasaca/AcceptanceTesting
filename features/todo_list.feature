Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries |
      | Pay bills     |
    When the user lists all tasks
    Then the output should contain:
      | Task         |
      | Buy groceries |
      | Pay bills     |

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | Task         | Status  |
      | Buy groceries | Pending |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries |
      | Pay bills     |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Add a duplicate task to the to-do list
    Given the to-do list contains tasks:
      | Task         |
      | Buy groceries |
    When the user adds a task "Buy groceries"
    Then the system should prevent the task from being added
    And the to-do list should still contain only:
      | Task         |
      | Buy groceries |

  Scenario: Mark a non-existent task as completed
    Given the to-do list contains tasks:
      | Task         | Status  |
      | Buy groceries | Pending |
    When the user marks task "Wash car" as completed
    Then the system should indicate that the task does not exist
    And the to-do list should remain unchanged:
      | Task         | Status  |
      | Buy groceries | Pending |