from behave import Then
import logging

logger = logging.getLogger("User steps")


@Then("The user was logged in as {member_type}")
def step_impl(context, member_type):
    logger.info("Check member type")
    response, status_code = context.rest_controller.get_members_boards_information()
    user_type = response[0]['memberType']
    assert status_code == 200, f"Expected status code 200, but got {status_code}"
    assert user_type == member_type, f"Wrong member type: {user_type}, should be: {member_type}"


@Then("The user is not deactivated")
def step_impl(context):
    logger.info("Check member status")
    response, status_code = context.rest_controller.get_members_boards_information()
    deactivated_status = response[0]['deactivated']
    assert status_code == 200, f"Expected status code 200, but got {status_code}"
    assert deactivated_status == False, f"Wrong member status: {deactivated_status}, should be: False"