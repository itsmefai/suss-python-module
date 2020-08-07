f = open('myplants_edited.txt', "r")
contents = f.read()

# Creating a dictionary to store the plant's information
plant_dict = {}
plant_list = []

for i in contents.split('\n\n'):
    plant_info = i.split('\n')
    plant_name = plant_info[0]

    plant_list.append(plant_info)

for i in plant_list[:-1]:
    plant_dict[i[0]] = {'Name': i[0],
                                      'Last Updated': i[1],
                                      'Information': i[2:]}
