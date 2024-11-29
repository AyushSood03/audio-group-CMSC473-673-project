import os
import csv
from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor, GenerationConfig
import torch
import time

# Define the folder where images are stored
image_folder = "/fs/class-projects/fall2024/cmsc473/c473g000/selectedframes/local-selectedframes"
output_file = "image_descriptions.csv"

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

    # Open the CSV file
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Image Name", "Description"])

        # Loop through each file in the folder
        for filename in os.listdir(image_folder):
            image_path = os.path.join(image_folder, filename)
            
            try:
                with Image.open(image_path).convert("RGB") as image:
                    start = time.time()

                    # Process the image and text
                    inputs = processor.process(
                        images=[image],
                        text=(
                            "Analyze the provided image and describe it in such a way that someone who cannot see the image can vividly imagine what it might sound like. Focus on the actions, atmosphere, and elements in the scene that suggest specific sounds or an ambiance. Avoid directly referencing visual details but instead translate them into auditory impressions. Your description should evoke a clear sense of the sounds and the mood of the scene."
                        )
                    )

                    # Move inputs to the correct device and make a batch of size 1
                    inputs = {k: v.to(device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")).unsqueeze(0) for k, v in inputs.items()}

                    # Generate output with max 200 new tokens, stop when "<|endoftext|>" is reached
                    output = model.generate_from_batch(
                        inputs,
                        GenerationConfig(max_new_tokens=200, stop_strings="<|endoftext|>"),
                        tokenizer=processor.tokenizer
                    )

                    # Only get generated tokens; decode them to text
                    generated_tokens = output[0, inputs['input_ids'].size(1):]
                    generated_text = processor.tokenizer.decode(generated_tokens, skip_special_tokens=True)

                    # Write the image name and description to the CSV file
                    writer.writerow([filename, generated_text])

                    # Print the generated text and time taken
                    print(f"{filename}: {generated_text}")
                    print("Time taken:", time.time() - start)
            
            except (IOError, Image.UnidentifiedImageError):
                # If the file is not a valid image, skip it
                print(f"Skipping file {filename}: not a valid image.")

    print(f"Descriptions saved to {output_file}")
