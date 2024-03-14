from behave import When
import logging

logger = logging.getLogger("Boards")


@When("The user creates an board named {board_name}")
def step_impl(context, board_name):
    context.rest_controller.create_board(board_name)