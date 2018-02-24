import os
output = open("output.txt", "w")
devices = open(r"devices.txt", "r")

for device in devices:
    reply = os.command("ping -n 1 " + device)
    if reply == 0:
        output.write("Up\n")
    else:
        output.write("Down\n")

output.close()
