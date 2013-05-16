import json
import re

# file = open("output.txt")
# textstr = file.readline()
# #print textstr
# jsontext = json.loads(textstr);

# if jsontext['text']:
# 	print 'good to go'
# 	print jsontext['text']

str = "fuck you  ggg "
print  re.split('\W*',str.lower())
