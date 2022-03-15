from venmo_api import Client
from venmo_api.apis.user_api import UserApi
from venmo_api.models.user import User
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
gclient = gspread.authorize(creds)
sheet = gclient.open("District Test")
worksheet1 = sheet.sheet1
try:
    worksheet2 = sheet.add_worksheet(title="Calculation Sheet", rows=100, cols = 26)
except:
    print("Did not create a duplicate sheet")
    worksheet2 = sheet.worksheet("Calculation Sheet")