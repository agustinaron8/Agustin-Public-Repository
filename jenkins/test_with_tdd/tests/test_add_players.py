import unittest

from source.team import Team

class TestTeamPlayers(unittest.TestCase):

    def test_(self) -> None:
        team = Team()
        team.add_players(6)
        self.assertEqual(team.players, 17)


if __name__ == '_main_':
    unittest.main()