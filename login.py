import json
import hashlib


def hash_password(password):
	h = hashlib.sha3_512(password.encode("UTF-8")).hexdigest()
	return h

credentials = {}

with open("creds.json", "r") as f:
	credentials = json.loads(f.read())

menu = int(input("Enter 1 to login and 2 to sign up: "))

if menu == 1:

	UserReq = input("What is your username: ")
	PassReq = hash_password(input("What is your password: "))

	try:
		if credentials[UserReq] == PassReq:
			print("Logged in!")
		else:
			print("Login failed!")
	except KeyError:
		print("Login failed!")

elif menu == 2:
	NewUser = input("Please select a username: ")
	NewPass = hash_password(input("Please select your password: "))

	try:
		credentials[NewUser]
		print("Username unavailable! Please select another.")
	except KeyError:
		credentials[NewUser] = NewPass
		print("Sign up succesful.")

with open("creds.json", "w") as f:
		f.write(json.dumps(credentials))
