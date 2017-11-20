import sys


class Player:
    VERSION = "Default Python folding player"
    
    def has_pair(card_list):
        count = [i for i in card_list if card_list.count(i) > 1]
        print len(count)
        if len(count) > 1:
            return true

    def betRequest(self, game_state):
        ourID = game_state["in_action"]
        card_1_rank = game_state["players"][ourID]["hole_cards"][0]["rank"]
        card_2_rank = game_state["players"][ourID]["hole_cards"][1]["rank"]
        #print card_1_rank
        #print card_2_rank
        high_rank = ["8", "9", "10", "J", "Q", "K", "A"]
        #highest_rank = ["J", "Q", "K", "A"]
        card_list = []
        card_list.append(card_1_rank)
        card_list.append(card_2_rank)
        if "community_cards" in game_state:
            for i in game_state["community_cards"]:
                card_list.append(i["rank"])
                #print i["rank"]
        #has_pair(card_list)
        count = [i for i in card_list if card_list.count(i) > 1]
        #print count
        #if len(count) >= 2 and (card_1_rank in highest_rank or card_2_rank in highest_rank or 
        if len(count) >= 2: 
            return game_state["current_buy_in"]
        if card_1_rank == card_2_rank:
            #print "pair"
            return game_state["current_buy_in"]
        if card_1_rank in high_rank or card_2_rank in high_rank: 
            #print "high"
            return game_state["current_buy_in"] - players["in_action"]["bet"]
        else:
            return 0

    def showdown(self, game_state):
        pass

