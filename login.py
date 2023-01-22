import json
import hashlib
import secrets


def hash_password(password, salt):
	p = f"{password}{salt}"
	h = hashlib.sha3_512(p.encode("UTF-8")).hexdigest()
	return h

credentials = {}

with open("creds.json", "r") as f:
	credentials = json.loads(f.read())
while True:
    menu = int(input("1) Login\n2) Sign Up\n3) Exit\n: "))

    if menu == 1:

        UserReq = input("What is your username: ")
        PassReq = input("What is your password: ")

        if type(credentials[UserReq]) != dict:
            if hashlib.sha3_512(PassReq.encode("UTF-8")).hexdigest() == credentials[UserReq]:
                NewSalt = secrets.randbits(512)
                NewPass = hash_password(PassReq, NewSalt)
                credentials[UserReq] = {"hash": NewPass, "salt": NewSalt}
                print("Logged in!")
            else:
                print("Login failed!")
        else:
            PassReq = hash_password(PassReq, credentials[UserReq]["salt"])

            try:
                if credentials[UserReq]["hash"] == PassReq:
                    print("Logged in!")
                else:
                    print("Login failed!")
            except KeyError:
                print("Login failed!")

    elif menu == 2:
        NewUser = input("Please select a username: ")
        NewSalt = secrets.randbits(512)
        NewPass = hash_password(input("Please select your password: "), NewSalt)

        try:
            credentials[NewUser]
            print("Username unavailable! Please select another.")
        except KeyError:
            credentials[NewUser] = {"hash": NewPass, "salt": NewSalt}
            print("Sign up succesful.")

    elif menu == 3:
        print("\nGoodbye!")
        break

with open("creds.json", "w") as f:
		f.write(json.dumps(credentials))
