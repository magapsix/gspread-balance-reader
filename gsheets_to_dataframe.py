
import pandas as pd
import gspread
import os
import json
from google.oauth2.service_account import Credentials

SPREADSHEET_ID = "1EFW0ZBsF0J5O4cZVHpqfpv9zFhpArzRt2zkaEPQuO3U"
SHEET_NAME = "Баланс"

# Завантаження облікових даних з змінної середовища
creds_dict = json.loads(os.environ["GOOGLE_SERVICE_ACCOUNT"])
creds = Credentials.from_service_account_info(creds_dict)
client = gspread.authorize(creds)

sheet = client.open_by_key(SPREADSHEET_ID)
worksheet = sheet.worksheet(SHEET_NAME)
data = worksheet.get_all_values()

headers = data[0]
rows = data[1:]

pp_balance_df = pd.DataFrame(rows, columns=headers)
print(pp_balance_df.head())
