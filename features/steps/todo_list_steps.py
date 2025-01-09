from behave import given, when, then
from todo_list import ToDoListManager

@given("the to-do list is empty")
def step_given_empty_todo_list(context):
    context.manager = ToDoListManager()

@when('the user adds a task "{task}"')
def step_when_user_adds_task(context, task):
    context.manager.add_task(task)

@then('the to-do list should contain "{task}"')
def step_then_todo_list_should_contain_task(context, task):
    tasks = context.manager.list_tasks()
    assert any(t["task"] == task for t in tasks), f"{task} not found in tasks."

@given('the to-do list contains tasks:')
def step_given_todo_list_contains_tasks(context):
    context.manager = ToDoListManager()
    for row in context.table:
        context.manager.add_task(row["Task"])

@when("the user lists all tasks")
def step_when_user_lists_all_tasks(context):
    context.tasks = context.manager.list_tasks()

@then("the output should contain:")
def step_then_output_should_contain(context):
    for row in context.table:
        assert any(t["task"] == row["Task"] for t in context.tasks), f"{row['Task']} not found in tasks."

@when('the user marks task "{task}" as completed')
def step_when_user_marks_task_completed(context, task):
    result = context.manager.mark_completed(task)
    assert result, f"Task {task} not found to mark as completed."

@then('the to-do list should show task "{task}" as completed')
def step_then_todo_list_should_show_task_completed(context, task):
    tasks = context.manager.list_tasks()
    for t in tasks:
        if t["task"] == task:
            assert t["status"] == "Completed", f"{task} is not marked as completed."
            return
    assert False, f"{task} not found in tasks."

@when("the user clears the to-do list")
def step_when_user_clears_todo_list(context):
    context.manager.clear_tasks()

@then("the to-do list should be empty")
def step_then_todo_list_should_be_empty(context):
    tasks = context.manager.list_tasks()
    assert len(tasks) == 0, "To-do list is not empty."

@then('the system should prevent the task from being added')
def step_then_prevent_task_addition(context):
    tasks = context.manager.list_tasks()
    assert len(tasks) == 1, "Duplicate task was added."

@then('the system should indicate that the task does not exist')
def step_then_task_not_found(context):
    result = context.manager.mark_completed("Wash car")
    assert not result, "Non-existent task was marked as completed."

@then('the to-do list should remain unchanged:')
def step_then_todo_list_unchanged(context):
    tasks = context.manager.list_tasks()
    for row in context.table:
        assert any(t["task"] == row["Task"] and t["status"] == row["Status"] for t in tasks), \
            f"{row['Task']} with status {row['Status']} is not in the list."
