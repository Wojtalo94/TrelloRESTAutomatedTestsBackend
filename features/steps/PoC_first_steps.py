from behave import Then
import logging

logger = logging.getLogger("PoC first test")


@Then("The user was logged in as {member_type}")
def step_impl(context, member_type):
    status = context.rest_controller.check_member_type()
    assert status == member_type, f"Wrong member type: {status}, should be: {member_type}"


@Then("The user is not deactivated")
def step_impl(context):
    status = context.rest_controller.check_member_deactivation()
    assert status == False, f"Wrong member status: {status}, should be: False"