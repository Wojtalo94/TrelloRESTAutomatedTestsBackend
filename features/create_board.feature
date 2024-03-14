Feature: Create board verification

    @board
    Scenario: The user is able to create a new board
        When The user creates an board named 'TestBoard'
        Then An board named 'TestBoard' has been created
        And Remove the board named 'TestBoard'
        And The board named 'TestBoard' has been removed