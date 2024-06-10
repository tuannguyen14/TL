import time
import json

data = open('save_file.json')
# data = json.loads(data[0])
for user in data[0]:
    print(user)
    time.sleep(3)