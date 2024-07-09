Feature: Home Page Functionality

  Background:
    Given the user loads Home page
    And the Home page is loaded

  Scenario: Verify user can fill email and password fields on home page "Test 1"
    When the email_input is displayed on Home page
    And the password_input is displayed on Home page
    And the signin_button is displayed on Home page
    Then the user fills email_input field on Home page with mahadev@633
    And the user fills password_input field on Home page with password

  Scenario: Verify list group values on home page "Test 2"
    When the Home page contains 3 test2_list_items_values elements
    Then the test2_second_list_item text on the Home page matches: List Item 2
    And the test2_second_list_item_bridge_value text on the Home page matches: 6

  Scenario: Verify select list functionality on home page "Test 3"
    When the user scrolls until test3_option_dropdown element is visible on the Home page
    And the test3_option_dropdown text on the Home page matches: Option 1
    Then the user clicks on test3_option_dropdown on Home page
    And the user clicks on test3_third_option on Home page
    And the test3_option_dropdown text on the Home page matches: Option 3

  Scenario: Verify button states on home page "Test 4"
    When the user scrolls until test3_option_dropdown element is visible on the Home page
    Then the user verifies that the test4_first_button element on the Home page is: enable
    And the user verifies that the test4_second_button element on the Home page is: disabled

  Scenario: Verify button click and success message on home page "Test 5"
    When the user scrolls until test5_button element is visible on the Home page
    And the user waits until test5_button element is clickable on the Home page
    Then the test5_alert_message text on the Home page matches: You clicked a button!

  Scenario: Verify the value of a cell in the table on home page "Test 6"
    When the user scrolls until test5_button element is visible on the Home page
    And the user gets the value from the cell at coordinates 2, 2 on Home page for element test6_grid_coordinates
    Then the value should be Ventosanzap
