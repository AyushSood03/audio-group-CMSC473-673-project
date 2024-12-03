import json

# Open and read the JSON file
with open('train.json', 'r') as file:
    audiocap = json.load(file)

with open('Audio_Captions_json.json', 'r') as file:
    Audio_Captions = json.load(file)
    
id_list = []
for item in Audio_Captions:
    current_id = item["image_id"]
    id_list.append(item["image_id"])

valid_id_list = []
temp_id_list = []
temp_annotations_list = []
for item in audiocap["images"]:
    if item["id"] in id_list:
        temp = {}
        temp["id"] = item["id"]
        temp_id_list.append(temp)
        valid_id_list.append(item["id"])
for item in audiocap["annotations"]:
    if item["id"] in id_list:
        temp = {}
        temp["id"] = item["id"]
        temp["image_id"] = item["id"]
        temp["caption"] = item["caption"]
        temp_annotations_list.append(temp)
        
temp_ground_truth = {}
temp_ground_truth["images"] = temp_id_list
temp_ground_truth["annotations"] = temp_annotations_list

temp_audio_captions = []
for item in Audio_Captions:
    if item["image_id"] in valid_id_list:
        temp_audio_captions.append(item)
        
        
temp_ground_truth_json = json.dumps(temp_ground_truth)
f = open("temp_ground_truth_json.json","w")
f.write(temp_ground_truth_json)
f.close()
        
temp_audio_captions_json = json.dumps(temp_audio_captions)
f = open("temp_audio_captions_json.json","w")
f.write(temp_audio_captions_json)
f.close()
               
        
        
        
    