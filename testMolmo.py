from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig
from PIL import Image
import requests
import torch
import time

with torch.no_grad():
    # load the processor
    processor = AutoProcessor.from_pretrained(
        'allenai/Molmo-7B-O-0924',
        trust_remote_code=True,
        torch_dtype="auto",
        device_map='auto',
        cache_dir='/fs/class-projects/fall2024/cmsc473/c473g000/hf_cache',
    )
    print('PROCESSOR')
    # print(processor.dtype)
    # load the model
    model = AutoModelForCausalLM.from_pretrained(
        'allenai/Molmo-7B-O-0924',
        trust_remote_code=True,
        torch_dtype="auto",
        device_map='auto',
        cache_dir='/fs/class-projects/fall2024/cmsc473/c473g000/hf_cache',
        )
    print('MODEL')
    print(model.dtype)

    start = time.time()
    # process the image and text
    inputs = processor.process(
        images=[Image.open(requests.get("https://picsum.photos/id/237/536/354", stream=True).raw)],
        text="Describe this image."
    )

    # move inputs to the correct device and make a batch of size 1
    inputs = {k: v.to(device=model.device).unsqueeze(0) for k, v in inputs.items()}

    # generate output; maximum 200 new tokens; stop generation when <|endoftext|> is generated
    output = model.generate_from_batch(
        inputs,
        GenerationConfig(max_new_tokens=200, stop_strings="<|endoftext|>"),
        tokenizer=processor.tokenizer
    )

    # only get generated tokens; decode them to text
    generated_tokens = output[0,inputs['input_ids'].size(1):]
    generated_text = processor.tokenizer.decode(generated_tokens, skip_special_tokens=True)

    # print the generated text
    print(generated_text)
    print(time.time()-start)
