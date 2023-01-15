stored_username = "testUser"
stored_password = "testPass"

UserReq = input("What is your username: ")
PassReq = input("What is your password: ")

if UserReq != stored_username or PassReq != stored_password:
    print("Login failed. Make sure you have typed in the correct characters and try again")
else:
    print("Login successful")