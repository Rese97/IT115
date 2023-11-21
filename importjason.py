#Importing the library of json.
import json


#Creating the data dictionary with diffrent data.

data = {

    'name': 'John Doe',
    'age':30,
    'city':'New york,NY',
    'interests': ['dancing','cooking','video games'],
    'is_student': True


}

#Writing and opening a file named data.json using the 'with' statement.
with open('data.json','w') as json_file:
    #Using json.dump to save the data with and indentation of 4 spaces.
    json.dump(data,json_file,indent=4)

print('data has been written to data.json')


# Reading data from the data.json file.
with open('data.json','r') as json_file:

    loaded_data = json.load(json_file)
#Print the content of the data.json file.
print("Successfully able to read data.json")
print(loaded_data)

#Changing the loaded data: change age to 34 and intrest to music.
loaded_data['age'] = 34
loaded_data['interests'].append('music')

#Wrting the data that has been modifed to data.json.
with open('data.json', 'w') as json_file:
    #Using json.dump to update the modified data.
    json.dump(loaded_data, json_file, indent=4)
#Confirming the file has been updated.
print('Modified data written to data.json.')


