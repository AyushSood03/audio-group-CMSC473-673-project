import os
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig
import torch
import time

# Define the folder where images are stored
image_folder = "/fs/class-projects/fall2024/cmsc473/c473g000/selectedframes"
output_file = "image_descriptions.txt"

# Load the processor and model
with torch.no_grad():
    processor = AutoProcessor.from_pretrained(
        'allenai/Molmo-7B-O-0924',
        trust_remote_code=True,
        torch_dtype="auto",
        device_map='auto',
        cache_dir='/fs/class-projects/fall2024/cmsc473/c473g000/hf_cache',
    )
    model = AutoModelForCausalLM.from_pretrained(
        'allenai/Molmo-7B-O-0924',
        trust_remote_code=True,
        torch_dtype="auto",
        device_map='auto',
        cache_dir='/fs/class-projects/fall2024/cmsc473/c473g000/hf_cache',
    )

    # Open the output file in write mode
    with open(output_file, "w") as f:
        # Loop through each file in the folder
        for filename in os.listdir(image_folder):
            image_path = os.path.join(image_folder, filename)
            
            # Try opening the file as an image
            try:
                with Image.open(image_path).convert("RGB") as image:
                    start = time.time()

                    # Process the image and text
                    inputs = processor.process(
                        images=[image],
                        # text="Describe this image."
                        text = (
                            "Describe what this image might sound like, focusing on actions, atmosphere, and any background elements that suggest sounds."
                            # "Generate a detailed description of this image, focusing on the main subject, its actions, and surroundings. "
                            # "Include sensory details that evoke the atmosphere, emotions, and possible sounds in the scene. "
                            # "Describe any visible objects, their colors, and the setting to help imagine the scene in both visual and auditory terms."
                        )
                    )

                    # Move inputs to the correct device and make a batch of size 1
                    inputs = {k: v.to(device=model.device).unsqueeze(0) for k, v in inputs.items()}

                    # Generate output with max 200 new tokens, stop when "<|endoftext|>" is reached
                    output = model.generate_from_batch(
                        inputs,
                        GenerationConfig(max_new_tokens=200, stop_strings="<|endoftext|>"),
                        tokenizer=processor.tokenizer
                    )

                    # Only get generated tokens; decode them to text
                    generated_tokens = output[0, inputs['input_ids'].size(1):]
                    generated_text = processor.tokenizer.decode(generated_tokens, skip_special_tokens=True)

                    # Save the result in the specified format
                    f.write(f"{filename} - '{generated_text}'\n")

                    # Print the generated text and time taken
                    print(f"{filename}: {generated_text}")
                    print("Time taken:", time.time() - start)
            
            except (IOError, Image.UnidentifiedImageError):
                # If the file is not a valid image, skip it
                print(f"Skipping file {filename}: not a valid image.")

    print(f"Descriptions saved to {output_file}")