Feature: Create board verification

    @board
    Scenario: The user is able to create a new board
        When The user creates an board named 'TestBoard'
        Then An board named 'TestBoard' has been created


    @board
    Scenario: The user is able to change board name
        When The user renames the board to 'T'
        # tutaj zrobić scenario outline z różnymi nazwami tablicy, w tym dużo i mało liter, znaki specjalne, cyfry itp, a ostatnia nazwa żeby była TestBoard
    

    @board
    Scenario: The user is able to delete board
        When Remove the board
        And The board has been removed
    