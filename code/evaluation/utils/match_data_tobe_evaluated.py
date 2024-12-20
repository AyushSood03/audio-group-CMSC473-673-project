import json
#This file checks the overlapped data points between the ground truth json and automated generated data points json by our pipeline. 
#Two temp .json file are created. These two json files can be directly inputted into Evaluation metrics.
#The file need to be run only when data points in ground truth json is different from automated generated data points json.

# Ground Truth json
with open('Audiocaps_train_and_val.json', 'r') as file:
    audiocap = json.load(file)

# Automated generated caption json
with open('Audiocaps_extra_data.json', 'r') as file:
    Audio_Captions = json.load(file)

# All youtube_ids in the json generated by our pipeline is added to id_list, waiting to be compared.
id_list = []
for item in Audio_Captions:
    current_id = item["image_id"]
    id_list.append(item["image_id"])

# valid_id_list has overlapped data points in it
# This session constructs the desired format of ground truth json with only overlapped datapoints  
# The format of the desired json file can be found in "Evaluation/example/references_format_example.json"
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

# This session constructs the desired format of automated generated captions json with only overlapped datapoints  
# The format of the desired json file can be found in "Evaluation/example/captions_format_example.json"
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
               
        
        
        
    
