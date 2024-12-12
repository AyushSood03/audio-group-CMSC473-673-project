import csv
import json
Audiocap_csv = []
with open('train.csv', encoding='utf8',mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        Audiocap_csv.append(lines)
with open('val.csv', encoding='utf8',mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        Audiocap_csv.append(lines)
#Audiocap_csv = Audiocap_csv[1:1501]

id_list = []
caption_list = []
for i in Audiocap_csv:
    id_list.append(i[1])
    caption_list.append(i[3])

non_duplicate_dict = {}
for index in range(len(id_list)):
    non_duplicate_dict[id_list[index]] = caption_list[index]



image_id_list = []
annotation_list = []

for file_id,caption in non_duplicate_dict.items():
    temp_dict = {}
    temp_dict["id"] = file_id
    image_id_list.append(temp_dict)

    temp_dict = {}
    temp_dict["id"] = file_id
    temp_dict["image_id"] = file_id
    temp_dict["caption"] = caption
    annotation_list.append(temp_dict)



'''
for i in range(1500):
    temp_dict = {}
    temp_dict["id"] = id_list[i]
    image_id_list.append(temp_dict)

    temp_dict = {}
    temp_dict["id"] = id_list[i]
    temp_dict["image_id"] = id_list[i]
    temp_dict["caption"] = caption_list[i]
    annotation_list.append(temp_dict)
    '''
json_dict = {}
json_dict["images"] = image_id_list
json_dict["annotations"] = annotation_list

real_json = json.dumps(json_dict)
f = open("Audiocaps_train_and_val.json","w")
f.write(real_json)
f.close()