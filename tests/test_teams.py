from cricbuzz.database_service.teamDAO import TeamDAO
from unittest.mock import MagicMock, patch


# def test_get_all_teams():
#     teams = get_all_teams()
#     assert len(teams) > 0

def test_get_all_teams_with_mocked_db():
    # Mocking the database function 'get_all_teams'
    with patch('cricbuzz.database_service.teamDAO.get_all_teams') as mock_get_all_teams:
        # Set the return value of the mocked function
        mock_get_all_teams.return_value = [
            [
                {
                    "team_id": 1,
                    "team_name": "India",
                    "team_country": "India",
                    "team_captain": "Rohit Sharma",
                    "team_coach": "Rahul Dravid"
                },
                {
                    "team_id": 2,
                    "team_name": "Australia",
                    "team_country": "Australia",
                    "team_captain": "Pat Cummins",
                    "team_coach": "Andrew McDonald"
                },
                {
                    "team_id": 3,
                    "team_name": "Pakistan",
                    "team_country": "Pakistan",
                    "team_captain": "Babar Azam",
                    "team_coach": "Grant Bradburn"
                },
                {
                    "team_id": 4,
                    "team_name": "New Zealand",
                    "team_country": "New Zealand",
                    "team_captain": "Kane Williamson",
                    "team_coach": "Gary Stead"
                },
                {
                    "team_id": 5,
                    "team_name": "South Africa",
                    "team_country": "South Africa",
                    "team_captain": "Temba Bavuma",
                    "team_coach": "Rob Walter"
                },
                {
                    "team_id": 6,
                    "team_name": "England",
                    "team_country": "England",
                    "team_captain": "Jos Buttler",
                    "team_coach": "Matthew Mott"
                },
                {
                    "team_id": 7,
                    "team_name": "Sri Lanka",
                    "team_country": "Sri Lanka",
                    "team_captain": "Dasun Shanaka",
                    "team_coach": "Chris Silverwood"
                },
                {
                    "team_id": 8,
                    "team_name": "Netherlands",
                    "team_country": "Netherlands",
                    "team_captain": "Scott Edwards",
                    "team_coach": "Ryan ten Doeschate"
                },
                {
                    "team_id": 9,
                    "team_name": "Bangladesh",
                    "team_country": "Bangladesh",
                    "team_captain": "Shakib Al Hasan",
                    "team_coach": "Chandika Hathurusingha"
                },
                {
                    "team_id": 10,
                    "team_name": "Afghanistan",
                    "team_country": "Afghanistan",
                    "team_captain": "Hashmatullah Shahidi",
                    "team_coach": "Jonathan Trott"
                }
            ]
        ]

        # Your test code that interacts with the mocked database function
        dao = TeamDAO()
        teams = dao.get_all_teams()

        # Assertion to verify the behavior based on the mocked database data
        assert len(teams) == 10
        # Add further assertions based on the expected behavior of your function
