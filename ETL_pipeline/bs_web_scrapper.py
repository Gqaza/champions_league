# %%
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


# %%
# Scrap teams data
res = requests.get(
    "https://www.skysports.com/football/teams"
).content
soup = bs(res, "html.parser")


league_teams_df = pd.DataFrame(
    columns=["team", "league"]
)
leagues = soup.findAll("optgroup")
for league in leagues:
    league_name = league.get("label")
    teams = league.findAll("option", class_="page-nav__select-option")
    dict_ = {}
    for team in teams:
        dict_['team'] = team.text
        dict_['league'] = league_name
        league_teams_df = league_teams_df.append(
            dict_, ignore_index=True
        )

league_teams_df.head()

# %%
"""
Add data to db
"""


# %%
r = requests.get("https://www.skysports.com/champions-league-table/2020").content  # noqa E501
soup = bs(r, "html.parser")

# %%
tables = soup.findAll("table", class_="standing-table__table")

headers_html = tables[0].find_all("th")
headers = [header.text for header in headers_html][:-1]

# %%
df = pd.DataFrame(columns=headers)
df["group"] = ""
df["season"] = ""

# %%
try:
    for table in tables:
        caption = table.find("caption").text
        group, season = caption.split("-")[-1].split()[1:]

        for row in table.find_all("tr")[1:]:
            row_entries = row.find_all("td")
            row_dict = {}
            for idx, r in enumerate(row_entries[:-1]):
                row_dict[f"{headers[idx]}"] = r.text
                row_dict["group"] = group
                row_dict["season"] = season
            df = df.append(row_dict, ignore_index=True)
except Exception as e:
    print(e)

# %%
df = df.rename(
    columns={
        "#": "league_position",
        "PI": "match_played",
        "W": "win",
        "D": "draw",
        "L": "loss",
        "F": "goals_for",
        "A": "goals_against",
        "GD": "goal_diff",
        "Pts": "points",
    }
)
df.head()
# %%

"""
TODO :

    1. format the data accordingly (e.g. df.Team)
    2. Update df.columns to match column names reflected in the models
    3. Push the data to the DB
    4. Update the get data for the following tables: player & team

"""

# %%


# %%
