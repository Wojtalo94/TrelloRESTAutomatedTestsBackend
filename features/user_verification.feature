Feature: User verification

    @user
    Scenario: Check user
        When The user creates an board named 'TestBoard'
        Then The user was logged in as admin
        And The user is not deactivated
        And Remove the board
        And The board has been removed