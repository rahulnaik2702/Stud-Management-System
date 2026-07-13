import json
from pathlib import Path

Database = "school_data.json"
data = {"students": [],"teachers" : []}

if Path(Database).exists():         
    with open(Database,'r') as f:
        content = f.read()
        if content:
            data = json.loads(content)

def save():
    with open(Database,"w") as f:
        json.dump(data,f,indent=4)