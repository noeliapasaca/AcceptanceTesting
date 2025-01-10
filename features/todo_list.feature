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

Scenario: Edit an existing task
  Given the to-do list contains tasks:
    | Task          | Status  |
    | Buy groceries | Pending |
  When the user edits the task "Buy groceries" to "Buy vegetables"
  Then the to-do list should contain:
    | Task          | Status  |
    | Buy vegetables | Pending |
  And the to-do list should not contain:
    | Task          |
    | Buy groceries |

Scenario: Filter tasks by completion status
  Given the to-do list contains tasks:
    | Task           | Status     |
    | Buy groceries  | Completed  |
    | Pay bills      | Pending    |
    | Do laundry     | Pending    |
  When the user filters tasks by "Pending"
  Then the output should contain only:
    | Task          |
    | Pay bills     |
    | Do laundry    |
  And the output should not contain:
    | Task          |
    | Buy groceries |
