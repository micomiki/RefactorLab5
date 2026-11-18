class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1points = 0
        self.player2points = 0
    


    def won_point(self, player_name):
        if player_name == "player1":
            self.player1points += 1
        else:
            self.player2points += 1
    def _equal_score(self):
       return {
             0: "Love-All",
             1: "Fifteen-All",
             2: "Thirty-All",
           }.get(self.player1points, "Deuce")
    

           
    def _endgame_score(self):
        point_difference = (
           self.player1points - self.player2points
          )

        if point_difference == 1:
           return "Advantage player1"
        elif point_difference == -1:
           return "Advantage player2"
        elif point_difference >= 2:
           return "Win for player1"
        else:
           return "Win for player2"

    
    def score(self):
        scores_are_equal = self.player1points == self.player2points
        either_player_reached_four = (
            self.player1points >= 4 or self.player2points >= 4
                )
        result = ""
        temp_score = 0
        if scores_are_equal:
            result = self._equal_score()
        elif either_player_reached_four:
            result = self._endgame_score()
        else:
            point_names = {
               0: "Love",
               1: "Fifteen",
               2: "Thirty",
               3: "Forty",
            }
            result = (
                f"{point_names[self.player1points]}-"
                f"{point_names[self.player2points]}"
            )

        return result
