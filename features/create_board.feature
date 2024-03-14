Feature: Create board verification

    @board @testing
    Scenario: The user is able to create a new board
        When The user creates an board named 'TestBoard'
        Then An board named 'TestBoard' has been created


    @board @testing
    Scenario Outline: The user is able to change board name
        When The user renames the board to <board_name> and description to <board_desc>
        Then Renamed the board to <board_name> and description to <board_desc>

        Examples: Settings
            | board_name                                               | board_desc                                               |
            | T                                                        | T                                                        |
            | 0                                                        | 0                                                        |
            | 1@T2$As*49Q*5-T_6Y '^'   "   7U8I9                       | 1@T2$As*49Q*5-T_6Y '^'   "   7U8I9                       |
            | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 1111111111111111111111111 | aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 1111111111111111111111111 |
            | TestBoard                                                | TestBoard                                                |
    

    @board @testing
    Scenario: The user is able to delete board
        When Remove the board
        Then The board has been removed
    