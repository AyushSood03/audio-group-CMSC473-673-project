import json
f = open("Audioset_GAMA_captions.txt","r")
existing_caption = f.readlines()
caption_dict = {}
index = 0
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

'''
f = open("Audiocaps_GAMA_captions.json","w")
f.write(real_json)
f.close()

'''