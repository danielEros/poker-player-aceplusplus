
class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        return game_state["current_buy_in"]

    def showdown(self, game_state):
        pass

