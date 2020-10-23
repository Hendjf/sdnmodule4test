"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""
import requests
from requests.auth import BearerToken

addresses = []

#asks user if they have an email address to enter, user must input yes or no
more = input("Do you have an email address to enter (y/n)? ")

#asks users to for email address to enter
while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
#Asks user to input another address
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")
#prints email addresses    
print(addresses)

URL ="https://webexapis.com/v1/memberships"
headers = {'Content-Type': 'application/json'}
response = requests.post(URL, auth=BearerToken, headers=headers, verify=False)

#converts our respone to json format and stores it in our variable resposneJSON

token = response.json()['NTg1M2VlMzgtMWMzZS00NDJiLWE4YWEtYTg2MGMwMjAxYmZmNDk5NjFlNTQtNmY3_PF84_7fe15fed-c67b-4ddc-b29c-39338b4d309e']

