import logging
from .Request import Request
from tools.user_data import UserData

class RestController():
    def __init__(self):
        self._logger = logging.getLogger("AppController")
        self._request = Request()
        _user_data = UserData("tools/user_data.csv")
        _api_key = _user_data.get_user_data("TRELLO_API_KEY")
        _api_token = _user_data.get_user_data("TRELLO_API_TOKEN")
        self.query_string = f"key={_api_key}&token={_api_token}"
        self.id = self._get_board_id(self.query_string)        

    def _get_board_id(self, query_string):
        self._logger.info("Get board id for next requests")
        response, _ = self._get_all_boards_data(query_string)
        first_board_id = response[0]['id']
        return first_board_id
    
    def _get_all_boards_data(self, query_string):
        response = self._request.get(f"https://api.trello.com/1/members/me/boards/?{query_string}")
        return response
    
    def check_member_type(self):
        self._logger.info("Check member type")
        response, _ = self._request.get_board(f"{self.id}/memberships?{self.query_string}")
        member_type = response[0]['memberType']
        return member_type

    def check_member_deactivation(self):
        self._logger.info("Check member status")
        response, _ = self._request.get_board(f"{self.id}/memberships?{self.query_string}")
        deactivated_status = response[0]['deactivated']
        return deactivated_status
    
    def create_board(self, board_name):
        self._logger.info(f"The user creates board named: {board_name}")
        self._request.post_board(f"?name={board_name}&{self.query_string}")
