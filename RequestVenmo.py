# Auto Request Payment on Venmo for meal prep meals
# TODO: have the excel auto populate the price fields, Create a program to auto pay the supplier, add a method to check if it was paid and mark it on the excel

from venmo_api import Client
from venmo_api.apis.user_api import UserApi
from venmo_api.models.user import User
import gspread
from oauth2client.service_account import ServiceAccountCredentials

Username = input("Enter your Username: ")
Password = input("Enter your Password: ")

access_token = Client.get_access_token(username=Username, password=Password)
client = Client(access_token=access_token)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
gclient = gspread.authorize(creds)
sheet = gclient.open("District Test").sheet1
    
def RequestMoney(Username, Price):
    users = client.user.search_for_users(query=Username)
    for user in users:
      client.payment.request_money(amount=Price, note="District Meals", target_user=user)

def main():
    rawUsernames = sheet.col_values(2)
    rawPrices = sheet.col_values(21)
    Usernames = rawUsernames[1:]
    Prices = rawPrices[1:]
    
    index = 0
    while True:
        if index == len(Usernames):
            break
        print(index)
        # RequestMoney(Usernames[index], Prices[index])
        index += 1

if __name__ == "__main__":
    main()