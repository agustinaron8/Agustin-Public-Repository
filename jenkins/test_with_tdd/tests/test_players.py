import unittest

from source.team import Team

class TestTeamPlayers(unittest.TestCase):

    def test_(self) -> None:
        team = Team()
        self.assertEqual(team.players, 11)


if __name__ == '_main_':
    unittest.main()