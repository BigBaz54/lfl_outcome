
""" 
DOESN'T TAKE TIEBREAKERS INTO ACCOUNT 
because it requires to take into account the whole record of the teams that are tied for the current split
"""


class Team():
    def __init__(self, name, wins, losses):
        self.name = name
        self.W = wins
        self.L = losses

    def __str__(self):
        return f'{self.name} : {self.W}W - {self.L}L'
    
    def win(self):
        self.W += 1

    def lose(self):
        self.L += 1

    def copy(self):
        return Team(self.name, self.W, self.L)

class League():
    def __init__(self, name, teams, matches_left):
        self.name = name
        self.teams = teams
        self.matches_left = matches_left
    
    def copy(self):
        teams = {e.name: e.copy() for e in self.teams.values()}
        return League(self.name+" copy", teams, self.matches_left.copy())

    def run_next_match(self, winner):
        match = self.matches_left[0]
        self.teams[match[winner]].win()
        self.teams[match[1-winner]].lose()
        self.matches_left.pop(0)

    def print_leaderboard(self):
        leaderboard = sorted(self.teams.values(), key=lambda team: team.W, reverse=True)
        for e in leaderboard:
            print(e)
        print('')

    def get_all_possible_outcomes(self):
        if self.matches_left == []:
            return [self]
        else:
            first_team = self.copy()
            first_team.run_next_match(0)

            second_team = self.copy()
            second_team.run_next_match(1)

            return first_team.get_all_possible_outcomes() + second_team.get_all_possible_outcomes()
        
    def print_all_possible_outcomes(self):
        for e in self.get_all_possible_outcomes():
            e.print_leaderboard()

    def get_qualified_teams(self):
        leaderboard = sorted(self.teams.values(), key=lambda team: team.W, reverse=True)
        return leaderboard[:6]
    
    def get_qualifying_odds(self):
        possible_outcomes = self.get_all_possible_outcomes()
        team_odds = {}
        for e in self.teams.values():
            team_odds[e.name] = 0
        for e in possible_outcomes:
            qualified = e.get_qualified_teams()
            for e in qualified:
                team_odds[e.name] += 1/len(possible_outcomes)
        return team_odds
    
    def print_qualifying_odds(self):
        for e in self.get_qualifying_odds().items():
            print(f"{e[0]} : {e[1]*100}%")



SLY = Team("Solary", 9, 8)
GW = Team("GameWard", 10, 7)
KC = Team("KCorp", 7, 10)
IZI = Team("IZI Dream", 2, 15)
VITB = Team("Vitality.Bee", 9, 8)
GO = Team("Team GO", 10, 7)
LDLC = Team("LDLC OL", 11, 6)
BDSA = Team("BDS Academy", 9, 8)
BKR = Team("BK ROG", 8, 9)
AEG = Team("AEGIS", 10, 7)

teams = {
    "Solary": SLY,
    "GameWard": GW,
    "KCorp": KC,
    "IZI Dream": IZI,
    "Vitality.Bee": VITB,
    "Team GO": GO,
    "LDLC OL": LDLC,
    "BDS Academy": BDSA,
    "BK ROG": BKR,
    "AEGIS": AEG
}

matches = [
    ("GameWard", "IZI Dream"),
    ("AEGIS", "Vitality.Bee"),
    ("Team GO", "KCorp"),
    ("LDLC OL", "BDS Academy"),
    ("Solary", "BK ROG")
]


LFL = League("LFL", teams, matches)


LFL.print_qualifying_odds()
