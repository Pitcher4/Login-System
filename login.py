credentials = {
	"testUser": "testPass",
	"gwo0d": "password123",
    "toby": "tobyisthebest"
}

UserReq = input("What is your username: ")
PassReq = input("What is your password: ")

try:
	if credentials[UserReq] == PassReq:
		print("Logged in!")
	else:
		print("Login failed!")
except KeyError:
	print("Login failed!")