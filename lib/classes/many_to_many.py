class Result:
    all = []
    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        Result.all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if hasattr(self, '_score'):
            print("Cannot reassign score")
        else:
            if isinstance(score, int):
                if 1 <= score <= 5000:
                    self._score = score

class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, '_title'):
            print('Cannot reassign title')
        else:
            if isinstance(title, str) and len(title):
                self._title = title
            else:
                print("Must be nonempty string")

    def results(self):
        game_list = []
        for result in Result.all:
            if result.game == self:
                game_list.append(result)
        return game_list

    def players(self):
        player_list = []
        final_list = []
        for result in Result.all:
            if result.game == self:
                player_list.append(result.player)
        player_set = set(player_list)
        for player in player_set:
            if isinstance(player, Player):
                final_list.append(player)
        return final_list

    def average_score(self, player):
        total = 0
        count = 0
        for result in Result.all:
            if result.game == self:
                if result.player == player:
                    total += result.score
                    count += 1
        return total/count

class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) >= 2 and len(username) <= 16:
            self._username = username
        else:
            print("Must be between 2 and 16 characters, inclusive")
    def results(self):
        results_list = []
        for result in Result.all:
            if result.player == self:
                results_list.append(result)
        return results_list

    def games_played(self):
        games_played = []
        final_list = []
        for result in Result.all:
            if result.player == self:
                games_played.append(result.game)
        games_set = set(games_played)
        for game in games_set:
            if isinstance(game, Game):
                final_list.append(game)
        return final_list

    def played_game(self, game):
        game_played = False
        for result in Result.all:
            if result.player == self:
                if result.game == game:
                    game_played = True
        return game_played
                


    def num_times_played(self, game):
        count = 0
        for result in Result.all:
            if result.player == self:
                if result.game == game:
                    count +=1
        return count


    
