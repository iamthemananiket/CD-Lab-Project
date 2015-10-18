import csv
from collections import OrderedDict
import json
json_list = []
json_file = open('MSCPES_1st_Round_SELECTED.json','w')
i=0
with open('MSCPES_1st_Round_SELECTED.csv', newline='') as f:
	reader = csv.reader(f)
	header = next(reader)
	for row in reader:
		dictionary = OrderedDict(zip(header,row))
		json_list.insert(i,dictionary)
		i=i+1
json_file.write(json.dumps(json_list,indent=4))
json_file.close()