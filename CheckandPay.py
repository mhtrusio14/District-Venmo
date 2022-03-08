from venmo_api import Client
from venmo_api.apis.user_api import UserApi
from venmo_api.models.user import User
import smtplib
from email.message import EmailMessage
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import pandas

client = Client(access_token='be07ca60fff9bcd25505af5db3139dd4c22c3dfa06dfcf5b50cf02f611bf7c2f')
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
gclient = gspread.authorize(creds)
sheet = gclient.open("District Test").sheet1

def sendText(name, amount):
    msg = EmailMessage()
    msg.set_content("Program just sent "+ name + " a Venmo request for " + amount)
    msg['subject'] = "Program sent Venmo Request"
    msg['to'] = "9738569653@vtext.com"
    user = "NetsCollector14@gmail.com"
    msg['from'] = user
    password = "abophtmwgsxxfrar"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

def GetUserTransactions():
    UserInfo = client.user.get_my_profile()
    transactions = client.user.get_user_transactions(user_id=UserInfo.id, limit=10)
    return transactions
        
def main():
    rawUsernames = sheet.col_values(2)
    rawPrices = sheet.col_values(21)
    Usernames = rawUsernames[1:]
    Prices = rawPrices[1:]
    transactions = GetUserTransactions()
    
    for transaction in transactions:
        time.sleep(20)
        # print(transaction.amount)
        # print("Actor: " + transaction.actor.username)
        # print("Target: " + transaction.target.username)
        index = 0
        while True:
            position = index + 2
            print(index+1)
            if index == len(Usernames):
                break
            if transaction.actor.username == Usernames[index] and transaction.amount == Prices[index] or transaction.target.username == Usernames[index] and transaction.amount == Prices[index]:
                sheet.update_cell(position,22,"Yes")
                break
            else:
                if sheet.cell(position, 22).value != "No":
                    sheet.update_cell(position,22,"No")
            index += 1
        
if __name__ == "__main__":
    main()
    