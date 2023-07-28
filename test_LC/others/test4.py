# import jwt
# key = "secret"
# # encoded = jwt.encode({"key": "value"}, key, algorithm="HS256")
# # print(encoded)
# decoded = jwt.decode("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJ2YWx1ZSJ9.FG-8UppwHaFp1LgRYQQeS6EDQF7_6-bMFegNucHjmWg", key, algorithms="HS256")
# print(decoded)  # {'key': 'value'}

# encoded = "eyJhbGciOiJIUzUxMiIsImlhdCI6MTY3MzM0Mjk0MywiZXhwIjoxNjc0NTUyNTQzfQ.ImV5SmhiR2NpT2lKSVV6STFOaUlzSW5SNWNDSTZJa3BYVkNKOS5leUoxYzJWeWFXUWlPalF3TENKeWIyeGxJanBiSW1Ga2JXbHVJbDBzSW1WNGNDSTZNVFkzTkRVNE1UTTBNMzAuSEZxS0N1V2diUWR0S0Y3cm5xSnZENHdzZC10YVlHdTlqQ3BPS0k1VmJvTSI.UuWENMI7Ad6Qn_IU3ot2WUqgF78w7AZuHabYBRxznBEYMOw8rksZ14lXiuszVzqgyeOC9FFswTQAQtb4zA_Jag"
# decoded = jwt.decode(encoded, key, algorithms="HS256")
# print(decoded)

import jwt
key = "secretblablablalalalala"
encoded = jwt.encode({"key": "value", "key2": "value2"}, key, algorithm="HS256")
# encoded2 = jwt.encode({"key": "value", "key2": "value2"}, key, algorithm="HS256", headers={"kid": "230498151c214b788dd97f22b85410a5"})
print(encoded)
# print(encoded2)
decoded = jwt.decode(encoded, algorithms="HS256", options={"verify_signature": False})  # 假设我不知道key，用这种方式也能解码出来。。。
decoded2 = jwt.decode(encoded, key, algorithms="HS256")
# decoded2 = jwt.decode(encoded2, key, algorithms="HS256")
print("decoded:", decoded)
print("decoded:", decoded2)

# # reading headers without validation
# print(jwt.get_unverified_header(encoded))  # {'alg': 'HS256', 'typ': 'JWT'}
# print(jwt.get_unverified_header(encoded2))  # {'alg': 'HS256', 'kid': '230498151c214b788dd97f22b85410a5', 'typ': 'JWT'}






