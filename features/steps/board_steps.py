from behave import When, Then
import logging

logger = logging.getLogger("Boards")


@When("The user creates an board named '{board_name}'")
def step_impl(context, board_name):
    logger.info(f"The user creates board named: {board_name}")
    context.rest_controller.create_board(board_name)


@Then("An board named '{board_name}' has been created")
def step_impl(context, board_name):
    logger.info(f"Checking if the {board_name} board has been created")
    response, status_code = context.rest_controller.get_board_information()
    get_board_name = response['name']
    assert status_code == 200, f"Expected status code 200, but got {status_code}"
    assert get_board_name == board_name, f"Wrong board name type: {get_board_name}, should be: {board_name}"


@Then("Remove the board named '{board_name}'")
def step_impl(context, board_name):
    logger.info(f"The user deletes an board named: {board_name}")
    context.rest_controller.delete_board()


@Then("The board named '{board_name}' has been removed")
def step_impl(context, board_name):
    logger.info(f"Checking if the {board_name} board has been deleted")
    response, status_code = context.rest_controller.get_board_information()
    assert status_code == 404, f"Expected status code 404, but got {status_code}"
    assert response == {}, f"Board still present: {response}, should be: None"