import json

def normalize_rgb(rgb_values):
    return [value/255 for value in rgb_values]

def ppm_to_json(ppm_file):
    try:
        # Open && read PPM file
        with open(ppm_file, 'r') as f:
            contents = f.read().splitlines()
        if contents[0] != 'P3':
            raise ValueError("Invalid PPM format, expected 'P3' but got", contents[0])
        i = 1
        # Skip comments
        while contents[i][0] == '#':
            i += 1
        width, height = map(int, contents[i].split())
        max_val = int(contents[i+1])
        contents = contents[i+2:]
    except Exception as e:
        print("An error occured while reading the PPM file: ",e)
        return
    # Initialize a list to store the image's pixels
    image = []
    row = []
    color_values = []
    i = 0
    # Iterate through each pixel's RGB values
    for value in contents:
        color_values.append(int(value))
        # If we have 3 RGB values, we have a pixel
        if (i+1)%3 == 0:
            # Normalize the RGB values (can be removed, if you prefer from 0 to 255)
            normalized_color_values = normalize_rgb(color_values)
            # Special use for other project
            if sum(normalized_color_values) == 0:
                normalized_color_values[2] = 0.01
            # end of special use
            row.append(normalized_color_values)
            color_values = []
            # If we have a full row, append it to the image
            if (i+1)%(3*width) == 0:
                image.append(row)
                row = []
        i += 1

    # Write the image's pixels to a JSON file
    with open('output.json', 'w') as f:
        json.dump(image, f)
