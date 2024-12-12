"audiocaps_gama_captions.txt" are .txt file of audio caption for 2658 audios in Audiocaps dataset.

"audioset_gama_captions.txt" are .txt file of audio caption for 8602 audios in Audioset dataset.

"audiocaps_molmo_captions.txt" are .txt file of VLM descriptions for 1882 keyframes in Audiocaps dataset.

"audioset_molmo_captions.txt" are .txt file of VLM descriptions for 7584 keyframes in Audioset dataset.



The format of these .txt file are:

	file_id_1
	audio_caption_1
	
	file_id_2
	audio_caption_2
	
	...

In "utils" folder, three files are provided for converting the dataset into evaluable json files.

	"Caption_to_json.py"  changes .txt file to a json file that can input to Evaluation_matrics.
	
	"Audiocaps_csv_to_json.py"  changes the original audiocaps dataset .csv file to a json file that can input to evaluation_matrics.

Be aware that the result json file of these two .py are different. The evaluation matrics takes caption and reference in different format.
For some reason, captions from VLM may requires " encoding='ISO-8859-1' " to read and write with.

	"match_data_tobe_evaluated.py" compares the file_ids in both the reference and caption json file. This is necessary when there are data points appear in either reference or caption but not both. 
The output of the code are two "temp" json files that are ready to be put inside evaluation matrices.

In all the .py files, please change the input and output file names according to the need.
