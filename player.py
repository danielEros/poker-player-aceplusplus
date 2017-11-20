import sys


class Player:
    VERSION = "Default Python folding player"


    def betRequest(self, game_state):
        ourID = game_state["in_action"]
        card_1_rank = game_state["players"][ourID]["hole_cards"][0]["rank"]
        card_2_rank = game_state["players"][ourID]["hole_cards"][1]["rank"]
        high_rank = ["10", "J", "Q", "K", "A"]
        keepable_pair = ["7", "8", "9", "10", "J", "Q", "K", "A"]
        card_list = []
        card_list.append(card_1_rank)
        card_list.append(card_2_rank)
        current_bid = game_state["current_buy_in"]
        color_list = []
        card_1_color = game_state["players"][ourID]["hole_cards"][0]["suit"]
        card_2_color = game_state["players"][ourID]["hole_cards"][1]["suit"]
        if "community_cards" in game_state:
            for i in game_state["community_cards"]:
                card_list.append(i["suit"])
        color_set = set(color_list)

        half_of_pair_in_hand = False
        if "community_cards" in game_state:
            for i in game_state["community_cards"]:
                card_list.append(i["rank"])
                if i["rank"] == card_1_rank or i["rank"] == card_2_rank:
                    half_of_pair_in_hand = True



        #has_pair(card_list)
        count = [i for i in card_list if card_list.count(i) > 1]

        #keepable-pair
        if len(count) >= 2 and count[0] in keepable_pair:
            return current_bid
        
        current_bet = game_state["current_buy_in"] - game_state["players"][ourID]["bet"]
        all_in = game_state["players"][ourID]["stack"]

        if game_state["players"][ourID]["bet"] > 100:
            return 0       
        if len(count) != 0 and (count[0] == "A" or count[0] == "K"):
            return all_in

        #pre-flop
        if len(card_list) <= 2:
            if current_bet > 0:
                return abs(current_bet)
            else:
                return current_bid
        
        if len(count) != 0 and (count[0] == "A" or count[0] == "K"):
            return all_in

        if len(card_list) > 2 and not half_of_pair_in_hand:
            return 0

        #color
        if len(card_list) > 2 and len(color_set) == 1:
            return current_bid

        #high-rank
        if card_1_rank in high_rank or card_2_rank in high_rank: 
            if current_bet > 0:
                return abs(current_bet)
            else:
                return current_bid
        return 0
           
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
 
    def showdown(self, game_state):
        pass

