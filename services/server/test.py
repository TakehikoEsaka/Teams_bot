import json
import os
# 正規表現練習用
import re
data = os.getenv("PEOPLE_NAME")
print(data)
data = "Yamamoto"
pattern = r"mamo"
result = re.match(pattern, data) #
print(result)
match = re.search(pattern, data)
print('password:', match.group())