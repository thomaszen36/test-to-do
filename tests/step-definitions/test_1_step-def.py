import time
import pytest
from pytest_bdd import given, when, then


@given("I navigate to todo website")
def navigate_to_todo_site(scenario_page) :
    # goto website
    scenario_page.goto("https://todomvc.com/examples/react/dist/")

@then("The new todo input field should be empty")
def assert_input_field_empty(scenario_page) :
    ?????????















######### IGNORE THIS #############
def test(scenario_page) :
    #goto google.com
    scenario_page.goto("https://todomvc.com/examples/react/dist/")
    time.sleep(5)
######### IGNORE THIS #############