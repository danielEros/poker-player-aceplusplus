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
        high_rank = ["10", "J", "Q", "K", "A"]
        keepable_pair = ["7", "8", "9", "10", "J", "Q", "K", "A"]
        #highest_rank = ["J", "Q", "K", "A"]
        card_list = []
        card_list.append(card_1_rank)
        card_list.append(card_2_rank)
        if "community_cards" in game_state:
            for i in game_state["community_cards"]:
                card_list.append(i["rank"])
                #print i["rank"]
        color_list = []
        
        #has_pair(card_list)
        count = [i for i in card_list if card_list.count(i) > 1]
        #print count
        #if len(count) >= 2 and (card_1_rank in highest_rank or card_2_rank in highest_rank or 
        if len(count) >= 2 and count[0] in keepable_pair: 
            return game_state["current_buy_in"]
        current_bet = game_state["current_buy_in"] - game_state["players"][ourID]["bet"]
        if card_1_rank in high_rank or card_2_rank in high_rank: 
            if current_bet > 0:
                return current_bet
            else:
                return game_state["current_buy_in"]
        if len(card_list) < 2:
            if current_bet > 0:
                return current_bet
            else:
                return game_state["current_buy_in"]
            
        """
        else:
            if current_bet > 0:
                stack = game_state["players"][ourID]["stack"]
                if current_bet < stack/3:
                    return current_bet
            else:
                return game_state["current_buy_in"]
            return 0
        """
        return 0

    def showdown(self, game_state):
        pass

