from venmo_api import Client
from venmo_api.apis.user_api import UserApi
from venmo_api.models.user import User
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
gclient = gspread.authorize(creds)
sheet = gclient.open("District Test").sheet1