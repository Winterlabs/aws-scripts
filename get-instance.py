'''
Nominated for FulHack 2017 - Best in show
'''

import json
from pprint import pprint
import subprocess

# http://boto.readthedocs.io/en/latest/getting_started.html

def find_key_value(list, key):
    for item in list:
        if item["Key"]==key:
            return item["Value"]


#https://stackoverflow.com/questions/17330139/python-printing-a-dictionary-as-a-horizontal-table-with-headers
def printTable(myDict, colList=None):
   """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson - Use it as you want but don't blame me.
   """
   if not colList: colList = list(myDict[0].keys() if myDict else [])
   myList = [colList] # 1st row = header
   for item in myDict: myList.append([str(item[col] or '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['-' * i for i in colSize]) # Seperating line
   for item in myList: print(formatStr.format(*item))


outputlist = []
outputdict = {}

cmd = 'aws ec2 describe-instances --output json'

proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
jsondata=proc.communicate()[0]

awsdata = json.loads(jsondata)

for res in awsdata["Reservations"]:
    for ii in res["Instances"]:
        print(ii["InstanceId"])
        print(find_key_value(ii["Tags"],"Name"))
#        print(ii["Instance"])


'''
pprint(j)

print j

#instance = json.loads()
'''
