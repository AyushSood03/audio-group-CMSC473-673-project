10/10/2024
Ayush: installed ffmpeg, got video -> audio conversion working
TODO next: add python code to read audio into array

10/15/2024
Xinchen Yu: Setting up environment for audio captioning model
Dat Dao: Setting up image captioning model.
Aishani: Cleaning AudioSet of Speech and Music and requested access to feature embeddings

10/17/2024
Xinchen Yu: API is not a good choice because queue is long. Seems like other users are doing their research. Trying to implement the model locally. For Nexus Pytorch implementation, a missing package may block the usage.

10/22/2024
Xinchen Yu: Doing conda setups.
Dat Dao: Setup env on the server + Research on the recent model for Image Captioning (pixtral/molmo)
Aishani: Eval and Balanced sets cleaned of speech and music erasing half of data from 20k to around 11k

10/24/2024
Xinchen Yu: It seems like conda virtual environment is constructed successfully. The API for LTU-AS works, trying to do the local inference. Need to find a way to convert sample rate to 16khz. Then cross-validation methods.

10/29/2024
Xinchen Yu: Trying to understand how gradio work, and how LTU-AS inference script work.

10/30/2024
Aishani: Received access to AudioSet feature tar but need to examine how to read tfrecords and audio embeddings
https://github.com/google/youtube-8m/blob/master/readers.py
https://stackoverflow.com/questions/46204992/how-can-i-extract-the-audio-embeddings-features-from-google-s-audioset

11/12/2024
Xinchen Yu: LTU-AS can run now, --mem=64G is needed to load all the models. The gradio page can be created now. However, it fails to give output. Need further debug to make it work. A bad news is that both the APIs for LTU and LTU-AS are dead. ERROR is shown on the huggingface gradio page. The UI of local inference gradio is different from the UI of the demo page LTU-AS (in my memory, since the page is down for some reason). Hopefully the models are the same.

11/14/2024 Xinchen Yu: LTU-AS requires ffmpeg for whisper feature extracting. However, the NEXUS server does not have packages for easy ffmpeg installation. ffmpeg python package is not working as well, since it looks like the whisper feature extracting code use local installed ffmpeg instead of a package. Manually extracting whisper feature also requires a lot of time for composing a json file for dataset. The next step is to try to implement GAMA.

11/19/2024 Xinchen Yu: GAMA successfully deployed on NEXUS server.
