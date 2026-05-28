import os

import requests
from dotenv import load_dotenv
from fastmcp import FastMCP

mcp = FastMCP("Football")

FOOTBALL_URL = "https://v3.football.api-sports.io/players?team=26&season=2022&league=1"

load_dotenv(override=True)

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY is not set in the environment variables")

headers = {
    "x-apisports-key": API_KEY
}

@mcp.tool()
def get_players_list_in_a_team(team_id: int) -> dict:
    """Get the list of all players in a team in the world cup 2022. It returns the player id and player name"""
    URL = f"https://v3.football.api-sports.io/players?team={team_id}&season=2022&league=1"
    response = requests.get(URL, headers=headers)
    return response.json()

@mcp.tool()
def get_player_stats(team_id: int, player_id: int) -> dict:
    """Get the stats of a player in the world cup 2022. It returns the player id, player name, team name, goals, assists, yellow cards and red cards"""
    URL = f"https://v3.football.api-sports.io/players?team={team_id}&id={player_id}&season=2022&league=1"
    response = requests.get(URL, headers=headers)
    return response.json()

@mcp.tool()
def get_team_list(team_id: int) -> dict:
    """Get the list of all teams in the world cup 2022. It returns the team id and team name"""
    URL = "https://v3.football.api-sports.io/teams?league=1&season=2022"
    response = requests.get(URL, headers=headers)
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="http")