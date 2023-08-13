import pandas as pd

df = pd.read_csv("YOUR_CSV_FILE_LINK")

!pip install gspread
from google.colab import auth
from google.auth import default
import gspread

auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)

planilha = gc.open("aula_df_to_gsheets")
aba1 = planilha.sheet1

aba1.update([df.columns.values.tolist()] + df.fillna(-1).values.tolist())


