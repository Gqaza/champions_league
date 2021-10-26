# %%
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


r = requests.get("https://www.skysports.com/champions-league-table/2020").content  # noqa E501
soup = bs(r, "html.parser")

# %%
tables = soup.findAll("table", class_="standing-table__table")

headers_html = tables[0].find_all('th')
headers = [header.text for header in headers_html][:-1]

# %%
df = pd.DataFrame(columns=headers)
df["Group"] = ""
df["Season"] = ""

# %%
try:
    for table in tables:
        caption = table.find("caption").text
        group, season = caption.split('-')[-1].split()[1:]

        for row in table.find_all('tr')[1:]:
            row_entries = row.find_all("td")
            row_dict = {}
            for idx, r in enumerate(row_entries[:-1]):
                row_dict[f"{headers[idx]}"] = r.text
                row_dict["Group"] = group
                row_dict["Season"] = season
            df = df.append(row_dict, ignore_index=True)
except Exception as e:
    print(e)

# %%
df = df.rename(columns={'#': 'Position'})
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
