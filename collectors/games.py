import pandas
# import numpy
import nba_api
import requests
# import sqlalchemy
# import matplotlib
# import plotly


from nba_api.stats.endpoints import leaguegamefinder

games = leaguegamefinder.LeagueGameFinder().get_data_frames()[0]

print(games.columns)
print(games.head())

game_id = "0042500405"

from nba_api.stats.endpoints import PlayByPlayV3

pbp = PlayByPlayV3(game_id=game_id)

df = pbp.get_data_frames()[0]

print(df.columns)
print(df.head())