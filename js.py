import json

with open("sample-data.json") as file:
    data = json.load(file)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn = attrs.get("dn", "")
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")
    
    print(f"{dn} {descr} {speed} {mtu}")