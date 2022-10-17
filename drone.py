import command
import json
from dotenv import load_dotenv

load_dotenv()

res = command.run(['drone', "server", "ls"])
data = res.output
data = data.decode()
splts = data.split("\n")

arr = []
errorCount = 0
creating = 0
running = 0
pending = 0
shutdown = 0
staging = 0
stopped = 0
stopping = 0
created = 0
for i in splts:
    info = command.run(['drone', "server", "info", i])
    info_data = res.output
    decodes = info_data.decode()
    splitings = decodes.split("\n")
    print(splitings)
    b = {}
    for a in splitings:
        if "Name" in a:
            b["Name"] = a.replace("Name: ", "")
        elif "Address" in a:
            b["Address"] = a.replace("Address: ", "")
        elif "Region" in a:
            b["Region"] = a.replace("Region: ", "")
        elif "Size" in  a:
            b["Size"] = a.replace("Size: ", "")
        elif "State" in a:
            b["State"] = a.replace("State: ", "")
            if "running" in a:
                running += 1
            elif "creating" in a:
                creating += 1
                # command.run(['drone', "server", "destroy", i])
            elif "created" in a:
                created += 1
            elif "error" in a:
                errorCount += 1
                # command.run(['drone', "server", "destroy", i])
            elif "pending" in a:
                pending += 1
            elif "shutdown" in a:
                shutdown += 1
            elif "staging" in a:
                staging += 1
            elif "stopped" in a:
                stopped += 1
            elif "stopping" in a:
                stopping += 1
        elif "Error" in a:
            b["Error"] = a.replace("Error: ", "")
    arr.append({i: b})

print(f"Total running instance: {len(arr)}")

summary = {
    "summary": {
        "created": created,
        "creating": creating,
        "running": running,
        "error": errorCount,
        "pending": pending,
        "shutdown": shutdown,
        "staging": staging,
        "stopping": stopping,
        "stopped": stopped,
        "total": len(arr)
    }
}

arr.append(summary)


jsonString = json.dumps(arr, indent=4)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

res.exit