from termcolor import colored
from pathlib import Path
import shlex

input_name = ""
trim_choice = ""
trim_start = ""
trim_len = ""
output_name = ""
confirmation = ""

#####     ffmpeg Scripts     #####
global encode_passthru
global encode_timestamps
global mux


encode_timestamps = shlex.split(
    'ffmpeg -vsync -1 -ss {trim_start} -i "{input_name}" -to {trim_len} -crf 16 -c:v libx264 -profile:v high10 -level:v 4.0 -c:a copy -movflags +faststart "{output_name}"')
mux = shlex.split(
    'ffmpeg -ss {trim_start} -i "{input_name}" -t {trim_len} -map 0 -c copy -avoid_negative_ts make_zero "{output_name}"')


#####   Validate File Input     #####
def input_valid():
    while True:
        global input_name
        input_name = input(
            colored("What's our input file's name?: ", "light_magenta"))
        input_path = Path(f'{Path.cwd()}/{input_name}')
        print()
        print(input_path)
        if input_path.is_file():
            print(colored("File has been found in directory.", "green"))
            print()
            break
        else:
            print(colored(
                "This file doesn't exist in this directory. Check if the file was spelled correctly and try again.", "light_red"))
            print()
    return (input_name)


def encode_passthru():
    encode_input = f'ffmpeg -vsync -1 -i "{input_name}" -crf 16 -c:v libx264 -profile:v high10 -level:v 4.0 -c:a copy -movflags +faststart "{output_name}.mp4"'
    str(encode_input)
    encode = encode_input
    shlex.split(encode)
    return (encode)
