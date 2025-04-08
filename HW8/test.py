import json_db 

# json_db.insert({})

json_db.load()

# json_db.insert({"name": "test"})
json_db.insert_toy("Ball", 10.444, (0, 16))
json_db.insert_toy("Rocket", 99.99, (14, 16))
json_db.insert_toy("Gun", 499.99, (14, 16))

json_db.safe_close()

