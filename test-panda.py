import gspread
import pandas as pd

gc = gspread.service_account(filename='C:/Users/Ad_si/Downloads/sheets-python-test-333714-57825dc8750c.json')
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1FT3Jau5n1kYi3nSl1w9W3eVWmGDanUSUhsTy0XEEUjM/edit#gid=0')

worksheet = sh.worksheet('Gry')

records_data = worksheet.get_all_records()

records_df = pd.DataFrame.from_dict(records_data)

print(records_df.head())