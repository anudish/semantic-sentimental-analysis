import pprint
import requests
import re
import pymongo
import json

secret = '109d513e290a43858d4bcc5c8d3b91c7'
url = 'https://newsapi.org/v2/everything?'
newsData=[]
newsNumber=0
filepath = "D:\\Dalhousie\\Data Warehousing\\Assignment 4\\APItextfiles\\"
searchList = ["Canada","University","Dalhousie University","Halifax","Business"]
for searchName in searchList:
	parameters = {
		'q' : searchName,
		'pageSize' : 100,
		'apiKey' : secret
		}

	response = requests.get(url,params = parameters)
	response_json = response.json()
	print(response_json)

	for i in response_json['articles']:
		name = filepath+"newsData_"+ str(newsNumber) + ".txt"
		with open(name, 'w+', encoding='utf-8') as file:
			j = i['content']
			j = re.sub(r'(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)',' ',str(j))
			j = j.strip()
			datanews = "Title : " + str(i['title']) +" Content : " + j + " Description : " + str(i['description'])
			file.write(datanews)
		newsNumber = newsNumber + 1