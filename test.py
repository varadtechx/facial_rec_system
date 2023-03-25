import requests
import json
import os


input_folder = os.path.join(os.getcwd(), 'original_img')
output_folder = os.path.join(os.getcwd(), 'final_img')
filename=input("Enter Image name manually :  ")


#API endpoint URL
url = "https://api.deepai.org/api/image-editor"

modifications = [
    {"name": "add_beard"},
    {"name": "add_mustache"}
]

api_key = " 9c1d750c-aae7-474c-88f2-90872732e8ba "


input_image_path = os.path.join(input_folder, filename)

# style_image_url = "https://img.freepik.com/premium-photo/handsome-bearded-man-with-long-lush-beard-moustacheon-grey-background_265223-33389.jpg"

# Set the target mask (e.g. "beard", "moustache", or "mask")
# target_mask =  " beard "

# Set the output image path
# output_image_path = output_folder

payload = {
    'api-key': api_key,
    'image': open(input_image_path, 'rb'),
    'operations': json.dumps(modifications),
    'output': 'save',
    'save_as': output_folder
}

with open(input_image_path, 'rb') as f:
    files = {'input': f}
    response = requests.post(url, data=payload, files=files)


result = json.loads(response.text)
print(response.text)

if 'error' in result:
    # Print the error message
    print(result['error'])
else:
    # Print the output image path
    print(f"Output image saved at {output_folder}")



output_response = requests.get(output_url)
with open(output_folder, 'wb') as f_output:
    f_output.write(output_response.content)


print(result['output_url'])




