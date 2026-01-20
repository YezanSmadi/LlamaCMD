import subprocess
import time
from termcolor import colored
import llama_menu
import llama_scripts
import re
import os


#####   File Encoding   #####
def llama_encode(trim_choice, confirmation, timestamp):
    # Let's get encoding

    global output_name
    global trim_start
    global trim_len
    print(colored("Alright so you want to ", "cyan", attrs=[
          "bold", "underline"]) + colored("re-encode", "light_yellow", attrs=["bold", "underline"]))
    llama_scripts.input_valid()
    while True:
        trim_choice = input(colored("Would you like to trim the clip as well? ",
                            "light_magenta") + colored("[y/N]: ", "cyan")).strip()
        if trim_choice.lower() == "y":
            while True:
                trim_start = input(colored("Where would you like the trimmed video to start? ",
                                           "light_magenta") + colored("(Input HH:MM:SS): ", "cyan")).strip()
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
                    "And how long would you like the trimmed video to be? ", "light_magenta") + colored("(Input HH:MM:SS): ", "cyan")).strip()
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
                                            "light_magenta") + colored("(ex. Output Encode.mp4): ", "cyan")).strip()
                print()
                print(colored(
                    "Okay, so we're ", "light_magenta") + colored(f"trimming and re-encoding {llama_scripts.input_name} ", "light_yellow") + colored("starting from ", "light_magenta") +
                    colored(trim_start, "light_yellow") + colored(" for ", "light_magenta") + colored(trim_len, "light_yellow") + colored(" long, with the name of ", "light_magenta") + colored(output_name, "light_yellow") +
                    colored(".", "light_magenta"))
                confirmation = input(
                    colored("Continue?", "light_magenta") + colored(" [y/N]: ", "cyan")).strip()
                if confirmation.lower() == "y":
                    subprocess.call(llama_scripts.encode_trim_passthru(
                        output_name, trim_start, trim_len), shell=True)
                    llama_scripts.file_done()
                elif confirmation.lower() == "n":
                    print(colored(
                        "Operation cancelled. Heading back to home screen in 3 seconds...", "light_red"))
                    time.sleep(3)
                    llama_menu.home_screen()
                    break
                elif confirmation.lower() != "y" or "n":
                    print()
                    print(
                        colored("Invalid Answer. Please type either Y or N", "light_red"))
                    print()

        elif trim_choice.lower() == "n":
            print(colored("Alright, no trimming.", "cyan"))
            while True:
                output_name = input(colored("Give a name to your output file with a file extension ",
                                            "light_magenta") + colored("(ex. Output Encode.mp4): ", "cyan")).strip()
                print()
                print(colored("Okay, so we're ", "light_magenta") + colored("re-encoding ", "light_yellow") + colored("the entirety of ", "light_magenta") + colored(llama_scripts.input_name, "light_yellow") + colored(
                    " into ", "light_magenta") + colored(output_name, "light_yellow") + colored(". ", "light_magenta"))
                confirmation = input(
                    colored("Continue? [y/n]: ", "cyan")).strip()
                if confirmation.lower() == "y":
                    subprocess.call(llama_scripts.encode_passthru(
                        output_name), shell=True)
                    llama_scripts.file_done()
                    break
                elif confirmation.lower() == "n":
                    print(colored(
                        "Operation cancelled. Heading back to home screen in 3 seconds...", "light_red"))
                    time.sleep(3)
                    llama_menu.home_screen()
                    break
                elif confirmation.lower() != "y" or "n":
                    print()
                    print(
                        colored("Invalid Answer. Please type either Y or N", "light_red"))
                    print()

        elif trim_choice.lower() != "y" or "n":
            print()
            print(colored("Invalid Answer. Please type either Y or N", "light_red"))
            print()


#####   File Muxing     #####
def llama_mux():
    # Let's get muxing

    global output_name
    global trim_start
    global trim_len
    print(colored("Alright so you want to ", "cyan", attrs=[
          "bold", "underline"]) + colored("mux", "light_yellow", attrs=["bold", "underline"]))
    llama_scripts.input_valid()
    while True:
        trim_choice = input(colored("Would you like to trim the clip as well? ",
                            "light_magenta") + colored("[y/N]: ", "cyan")).strip()
        if trim_choice.lower() == "y":
            while True:
                trim_start = input(colored("Where would you like the trimmed video to start? ",
                                           "light_magenta") + colored("(Input HH:MM:SS): ", "cyan")).strip()
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
                    "And how long would you like the trimmed video to be? ", "light_magenta") + colored("(Input HH:MM:SS): ", "cyan")).strip()
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
                                            "light_magenta") + colored("(ex. Output Encode.mp4): ", "cyan")).strip()
                print()
                print(colored(
                    "Okay, so we're ", "light_magenta") + colored(f"trimming and muxing {llama_scripts.input_name}", "light_yellow") + colored(" starting from ", "light_magenta") +
                    colored(trim_start, "light_yellow") + colored(" for ", "light_magenta") + colored(trim_len, "light_yellow") + colored(" long, with the name of ", "light_magenta") + colored(output_name, "light_yellow") +
                    colored(".", "magenta"))
                confirmation = input(
                    colored("Continue?", "light_magenta") + colored(" [y/N]: ", "cyan")).strip()
                if confirmation.lower() == "y":
                    subprocess.call(llama_scripts.encode_trim_passthru(
                        output_name, trim_start, trim_len), shell=True)
                    llama_scripts.file_done()
                elif confirmation.lower() == "n":
                    print(colored(
                        "Operation cancelled. Heading back to home screen in 3 seconds...", "light_red"))
                    time.sleep(3)
                    llama_menu.home_screen()
                    break
                elif confirmation.lower() != "y" or "n":
                    print()
                    print(
                        colored("Invalid Answer. Please type either Y or N", "light_red"))
                    print()

        elif trim_choice.lower() == "n":
            print(colored("Alright, no trimming.", "cyan"))
            while True:
                output_name = input(colored("Give a name to your output file with a file extension ",
                                            "light_magenta") + colored("(ex. Output Encode.mp4): ", "cyan")).strip()
                print()
                print(colored("Okay, so we're ", "magenta") + colored("muxing", "light_yellow") + colored(" the entirety of ", "light_magenta") + colored(llama_scripts.input_name, "light_yellow") + colored(
                    " into ", "light_magenta") + colored(output_name, "light_yellow") + colored(". ", "light_magenta"))
                confirmation = input(
                    colored("Continue? [y/n]: ", "cyan")).strip()
                if confirmation.lower() == "y":
                    subprocess.call(llama_scripts.encode_passthru(
                        output_name), shell=True)
                    llama_scripts.file_done()
                    break
                elif confirmation.lower() == "n":
                    print(colored(
                        "Operation cancelled. Heading back to home screen in 3 seconds...", "light_red"))
                    time.sleep(3)
                    llama_menu.home_screen()
                    break
                elif confirmation.lower() != "y" or "n":
                    print()
                    print(
                        colored("Invalid Answer. Please type either Y or N", "light_red"))
                    print()

        elif trim_choice.lower() != "y" or "n":
            print()
            print(colored("Invalid Answer. Please type either Y or N", "light_red"))
            print()

##### Exit #####


def leave():
    llama_scripts.leave_llama()
    # Bye bye!
