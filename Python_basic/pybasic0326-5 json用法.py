import json
# with open("./data.json", encoding="UTF-8") as file:
#     #print(file.read())
#     object = json.loads(file.read())
#     #print(object["name"])
#     #print(object["b"])
#     for s in object:
#         print(f"{s["name"]} 分數:{s["scores"][2]}")

data = [
        {"name": "bob", "id": 1},
        {"name": "nier", "id": 2}
       ]
print(json.dumps(data))
json_from_data = json.dumps(data)
print(f"從物件來的字串 {json.dumps(data)}")

with open("frompython.json", "w", encoding="UTF-8") as file:
    file.write(json_from_data)

