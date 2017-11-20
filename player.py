import sys


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        ourID = game_state["in_action"]
        card_1_rank = game_state["players"][ourID]["hole_cards"][0]["rank"]
        card_2_rank = game_state["players"][ourID]["hole_cards"][1]["rank"]
        #print card_1_rank
        #print card_2_rank
        high_rank = ["8", "9", "10", "J", "Q", "K", "A"]
        if card_1_rank == card_2_rank:
            #print "pair"
            return game_state["current_buy_in"]
        if card_1_rank in high_rank or card_2_rank in high_rank: 
            #print "high"
            return game_state["current_buy_in"]
        else:
            return 0

    def showdown(self, game_state):
        pass

