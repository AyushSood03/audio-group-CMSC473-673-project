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
description = ""

for item in ori:
    current_dict = {}
    seperation_search = re.search(";;;;;;;;;;",item)
    if seperation_search  is not None:
        
        readable_list.append(current_dict)
        
        span = seperation_search.span()
        file_name = item[:span[0]]
        file_id = obtain_file_id(file_name)
        description = item[span[1]:]
        
        current_dict["image_id"] = file_id
        current_dict["caption"] = description[3:]
        continue
    description += item

real_json = json.dumps(readable_list)

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