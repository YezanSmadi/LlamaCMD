import subprocess
import time
from termcolor import colored
import llama_menu
import llama_scripts
import re
import os

##### File Encoding #####
global output_name
output_name = ""


def llama_encode(input_name, trim_choice, trim_start, trim_len, confirmation, output_name, timestamp):
    # Let's get encoding
    print(colored("Alright so you want to ", "cyan", attrs=[
          "bold", "underline"]) + colored("re-encode", "light_yellow", attrs=["bold", "underline"]))
    llama_scripts.input_valid()
    trim_choice = input(colored("Would you like to trim the clip as well? ",
                        "light_magenta") + colored("Type Y or N: ", "cyan"))
    if trim_choice.lower() == "y":
        while True:
            trim_start = input(colored("Where would you like the trimmed video to start? ",
                               "light_magenta") + colored("(Input HH:MM:SS): ", "cyan"))
            timestamp = r"\d\d:\d\d:\d\d"
            if re.match(timestamp, trim_start):
                break
            else:
                print()
                print(colored(
                    "Input invalid. It must be in the HH:MM:SS format (Hour(s), Minute(s), Second(s))", "light_red"))
                print()
        while True:
            trim_len = input(colored(
                "And how long would you like the trimmed video to be? ", "light_magenta") + colored("(Input HH:MM:SS): ", "cyan"))
            timestamp = r"\d\d:\d\d:\d\d"
            if re.match(timestamp, trim_len):
                break
            else:
                print()
                print(colored(
                    "Input invalid. It must be in the HH:MM:SS format (Hour(s), Minute(s), Second(s))", "light_red"))
                print()
        while True:
            output_name = input(colored("Give a name to your output file with a file extension ",
                                        "light_magenta") + colored("(ex. Output Encode.mp4): ", "cyan"))
            confirmation = input(colored(
                f"Okay, so we're trimming ", "light_magenta") + colored(llama_scripts.input_name, "light_yellow") + colored(" starting from ", "light_magenta") + colored(trim_start, "light_yellow") + colored(" for ", "light_magenta") + colored(trim_len, "light_yellow") + colored(" long, with the name of ", "light_magenta") + colored(output_name, "light_yellow") + colored(". Is that correct?", "light_magenta") + colored(" (Y or N): ", "cyan"))
            if confirmation.lower() == "y":
                subprocess.call(llama_scripts.encode_timestamps, shell=True)
            elif confirmation.lower() == "n":
                print(colored(
                    "Operation cancelled. Heading back to home screen in 3 seconds...", "light_red"))
                time.sleep(3)
                llama_menu.home_screen()
                break
            elif confirmation.lower() != "y" or "n":
                print()
                print(colored("Invalid Answer. Please type either Y or N", "light_red"))
                print()

    elif trim_choice.lower() == "n":
        print(colored("Alright, no trimming", "cyan"))
        while True:
            output_name = input(colored("Give a name to your output file with a file extension ",
                                        "light_magenta") + colored("(ex. Output Encode.mp4): ", "cyan"))
            confirmation = input(colored(f"Okay, so we're re-encoding the entirety of ", "light_magenta") + colored(llama_scripts.input_name, "light_yellow") + colored(
                " into ", "light_magenta") + colored(output_name, "light_yellow") + colored(". ", "light_magenta") + colored("Is that correct? (Y or N): ", "cyan"))
            encode_input = f'ffmpeg -vsync -1 -i "{input_name}" -crf 16 -c:v libx264 -profile:v high10 -level:v 4.0 -c:a copy -movflags +faststart "{output_name}"'
            print(encode_input)
            if confirmation.lower() == "y":
                subprocess.call(llama_scripts.encode_passthru(), shell=True)
            elif confirmation.lower() == "n":
                print(colored(
                    "Operation cancelled. Heading back to home screen in 3 seconds...", "light_red"))
                time.sleep(3)
                llama_menu.home_screen()
                break
            elif confirmation.lower() != "y" or "n":
                print()
                print(colored("Invalid Answer. Please type either Y or N", "light_red"))
                print()
    elif trim_choice.lower() != "y" or "n":
        print()
        print(colored("Invalid Answer. Please type either Y or N", "light_red"))
        print()


##### File Muxing #####
def llama_mux():
    # Muxing! A clean solution for changing containers.
    mux = ""


##### Exit #####
def leave():
    print(colored("Pleasure working with you!", "cyan"))
    print()
    exit()
    # Bye bye!
