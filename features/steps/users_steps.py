from behave import Then
import logging

logger = logging.getLogger("User steps")


@Then("The user was logged in as {member_type}")
def step_impl(context, member_type):
    logger.info("Check member type")
    status = context.rest_controller.get_members_boards_information()
    user_type = status[0]['memberType']
    assert user_type == member_type, f"Wrong member type: {user_type}, should be: {member_type}"


@Then("The user is not deactivated")
def step_impl(context):
    logger.info("Check member status")
    status = context.rest_controller.get_members_boards_information()
    deactivated_status = status[0]['deactivated']
    assert deactivated_status == False, f"Wrong member status: {deactivated_status}, should be: False"