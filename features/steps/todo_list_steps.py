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

@given(u'the to-do list contains tasks')
def step_impl(context):
    context.manager = ToDoListManager()  # Create a new To-Do List Manager
    for row in context.table:
        context.manager.add_task(row["Task"])

@when(u'the user lists all tasks')
def step_impl(context):
    context.tasks = context.manager.list_tasks()

@then(u'the output should contain')
def step_impl(context):
    for row in context.table:
        assert any(
            task["task"] == row["Task"] for task in context.tasks
        ), f"Task {row['Task']} is not in the output."

@when(u'the user marks task "{task}" as completed')
def step_impl(context, task):
    result = context.manager.mark_completed(task)
    assert result, f"Task {task} could not be marked as completed."

@then(u'the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    tasks = context.manager.list_tasks()
    for t in tasks:
        if t["task"] == task:
            assert t["status"] == "Completed", f"Task {task} is not marked as completed."
            return
    assert False, f"Task {task} is not found in the to-do list."

@when(u'the user clears the to-do list')
def step_impl(context):
    context.manager.clear_tasks()

@then(u'the to-do list should be empty')
def step_impl(context):
    tasks = context.manager.list_tasks()
    assert len(tasks) == 0, "The to-do list is not empty."

@when(u'the user edits the task "{old_task}" to "{new_task}"')
def step_impl(context, old_task, new_task):
    result = context.manager.edit_task(old_task, new_task)
    assert result, f"Task {old_task} could not be edited to {new_task}."

@then(u'the to-do list should contain')
def step_impl(context):
    tasks = context.manager.list_tasks()
    for row in context.table:
        assert any(
            task["task"] == row["Task"] and task["status"] == row["Status"]
            for task in tasks
        ), f"Task {row['Task']} with status {row['Status']} is not in the to-do list."

@then(u'the to-do list should not contain')
def step_impl(context):
    tasks = context.manager.list_tasks()
    for row in context.table:
        assert not any(
            task["task"] == row["Task"] for task in tasks
        ), f"Task {row['Task']} should not be in the to-do list."

@when(u'the user filters tasks by "{status}"')
def step_impl(context, status):
    context.filtered_tasks = context.manager.filter_tasks(status)

@then(u'the output should contain only')
def step_impl(context):
    expected_tasks = [row["Task"] for row in context.table]
    filtered_tasks = [task["task"] for task in context.filtered_tasks]

    # Debugging output for unexpected tasks
    unexpected_tasks = [task for task in filtered_tasks if task not in expected_tasks]
    assert not unexpected_tasks, f"Filtered output contains unexpected tasks: {unexpected_tasks}"

    # Check for missing tasks
    for expected_task in expected_tasks:
        assert expected_task in filtered_tasks, f"Task {expected_task} is missing from the filtered output."

@then(u'the output should not contain')
def step_impl(context):
    filtered_tasks = [task["task"] for task in context.filtered_tasks]
    for row in context.table:
        assert row["Task"] not in filtered_tasks, f"Task {row['Task']} should not be in the filtered output."




