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