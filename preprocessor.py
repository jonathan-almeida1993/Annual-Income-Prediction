#!/usr/bin/python3

#This program creates a list of unique feature values for each feature
#of the input data set and dumps everything into a .json file
#The age and hours list in the .json file don't matter, since they
#are going to be reinitialized anyway. This .json file can be 
#conviniently imported into a dictionary.

import json

#open file for reading data
file = open("income-data/income.train.txt","r");


age=[];
workclass=[];
education=[];
marital_status=[];
occupation=[];
race=[];
sex=[];
hours=[];
country=[];
target=[];

for line in file:
	features = line.split(",");
	if features[0].strip() not in age:
		age.append(features[0].strip());

	if features[1].strip() not in workclass:
		workclass.append(features[1].strip());

	if features[2].strip() not in education:
		education.append(features[2].strip());

	if features[3].strip() not in marital_status:
		marital_status.append(features[3].strip());

	if features[4].strip() not in occupation:
		occupation.append(features[4].strip());

	if features[5].strip() not in race:
		race.append(features[5].strip());

	if features[6].strip() not in sex:
		sex.append(features[6].strip());

	if features[7].strip() not in hours:
		hours.append(features[7].strip());

	if features[8].strip() not in country:
		country.append(features[8].strip());

	if features[9].strip() not in target:
		target.append(features[9].strip());

age.sort();
workclass.sort();
education.sort();
marital_status.sort();
occupation.sort();
race.sort();
sex.sort();
hours.sort();
country.sort();
target.sort();

dict = {"age":age,"workclass":workclass,"education":education,"marital_status":marital_status,"occupation":occupation,"race":race,"sex":sex,"hours":hours,"country":country,"target":target}

json = json.dumps(dict)
output = open("FEATURE_VALUES.json","w")
output.write(json)
output.close()
file.close()