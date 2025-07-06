# Website -

# As a user
# I want to add tasks to my todo list
# So that I can keep track of my tasks

# AC-
  # The input field is empty on page load
  # Typing text into input and pressing Enter adds a new item to the bottom of the list
  # The newly added item label matches exactly what was typed
  # The input field is cleared after pressing Enter

Feature: Add new todo items

  Scenario: Input field is empty on page load
    Given I navigate to todo website
    Then The new todo input field should be empty

  Scenario: Add single todo item
    Given I navigate to todo website
    When I type 'Buy milk' into new todo input and press Enter
    Then I should see a todo item with label 'Buy milk'
    And the new todo input should be empty

  Scenario: Add multiple todos
    Given I navigate to todo website
    When I add the following todos:
      | task          |
      | Buy groceries |
      | Water plants  |
    Then I should see 2 todo items
    And the items should be in order:
      | Buy groceries |
      | Water plants  |