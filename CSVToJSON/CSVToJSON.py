import csv	 											
from collections import OrderedDict
import json										#Inbuilt libraries
json_list = []									#List to store the JSON represntation
json_file = open('MSCPES_1st_Round_SELECTED.json','w')	#File that will have the JSON format
i=0
with open('MSCPES_1st_Round_SELECTED.csv', newline='') as f:	#Open the CSV file and place into 'f' with lines seperated by ''
	reader = csv.reader(f)										#Return a reader object
	header = next(reader)										#Read the first line that is the header
	for row in reader:											#Loop through the whole CSV file
		dictionary = OrderedDict(zip(header,row))				#Create an ordered dictionary by mapping the headers to rows
		json_list.insert(i,dictionary)							#insert each dictionary into the List
		i=i+1
json_file.write(json.dumps(json_list,indent=4))					#Convert list to JSON and write into seperate file
json_file.close()								
