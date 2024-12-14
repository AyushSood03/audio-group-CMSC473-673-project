import json
import numpy as np
import re

def obtain_file_id(name):
    length = len(name)
    start_index = length-1
    end_index = length-1
    index = length-1
    flag0 = 0
    flag1 = 0
    while flag0 != 1 or flag1 != 1:
        character = name[index]
        if character == ']':
            end_index = index
            flag1 = 1
        if character == '[':
            start_index = index
            flag0 = 1
        index -=1
    return name[start_index+1:end_index]
#NumpyCSV = np.genfromtxt("audiocap_desciption_ids.csv",encoding='UTF-8',delimiter=',')

f = open("audiocap_desciption.csv",encoding='ISO-8859-1',mode ='r')
ori = f.readlines()
f.close()
ori = ori[1:]
readable_list = []
file_name = ""
last_name = ""
description = ""
last_description = ""
id_list = []
description_list = []
index = -1
for item in ori:
    seperation_search = re.search(";;;;;;;;;;",item)
    if seperation_search is not None:
        index+=1
        span = seperation_search.span()
        file_name = item[:span[0]]
        file_id = obtain_file_id(file_name)
        id_list.append(file_id)
        description = item[span[1]:]
        description_list.append(description)
        #current_dict["image_id"] = file_id
        #current_dict["caption"] = description[3:]
        continue
    description_list[index] += item

#This step to eliminate duplication
non_duplicate_dict = {}
for index in range(len(id_list)):
    non_duplicate_dict[id_list[index]] = description_list[index]

VLM_json = []
for file_id,caption in non_duplicate_dict.items():
    current_dictionary = {}
    current_dictionary["image_id"] = file_id
    current_dictionary["caption"] = caption[3:]
    VLM_json.append(current_dictionary)

'''
for item in ori:
    current_dict = {}
    seperation_search = re.search(";;;;;;;;;;",item)
    if seperation_search is not None:
        
        readable_list.append(current_dict)
        
        span = seperation_search.span()
        file_name = item[:span[0]]
        file_id = obtain_file_id(file_name)
        description = item[span[1]:]
        
        current_dict[file_id] = description[3:]
        
        
        #current_dict["image_id"] = file_id
        #current_dict["caption"] = description[3:]
        
        continue
    description += item
'''

'''
VLM_json = []
for item in readable_list:
    current_dictionary = {}
    current_dictionary["image_id"] = list(item.keys())[0]
    current_dictionary["caption"] = item[list(item.keys())[0]]
    VLM_json.append(current_dictionary)



'''



real_json = json.dumps(VLM_json)

f = open("VLM_Captions_json.json","w")
f.write(real_json)
f.close()

'''
json_list = []
for pair in readable_list:
    pair.keys()
    temp = {}
    temp["image_id"] = image_id
    temp["caption"] = caption_dict[image_id]
    
    
    json_list.append(temp)
real_json = json.dumps(json_list)

f = open("Audio_Captions_json.json","w")
f.write(real_json)
f.close()

'''


'''
while index < len(existing_caption):
    caption_dict[existing_caption[index][:-1]] = existing_caption[index+1][:-1]
    index+=3
f.close()
print(len(caption_dict))
json_list = []
for image_id in caption_dict.keys():
    temp = {}
    temp["image_id"] = image_id
    temp["caption"] = caption_dict[image_id]
    
    
    json_list.append(temp)
real_json = json.dumps(json_list)

f = open("Audio_Captions_json.json","w")
f.write(real_json)
f.close()
'''