import sys


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print "ITTT   TT"
        sys.stderr.write("ERRROR WRITE ")
        return game_state["current_buy_in"]

    def showdown(self, game_state):
        pass

