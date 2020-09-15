import json
import sys

jfile = open('module.json')
jtext = json.load(jfile)

index = 0

arg = sys.argv
if len(arg) > 1:
    index = int(arg[1])
else:
    index = 0


print(jtext["members"][index])


