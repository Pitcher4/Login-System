"""
Note: Only to be run on unhashed creds.json file.
"""

"""
import json
import hashlib


def hash_password(password):
	h = hashlib.sha3_512(password.encode("UTF-8")).hexdigest()
	return h

credentials = {}

with open("creds.json", "r") as f:
	credentials = json.loads(f.read())

for key in credentials:
	credentials[key] = hash_password(credentials[key])

with open("creds.json", "w") as f:
		f.write(json.dumps(credentials))
"""