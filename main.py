import datetime
import sys

from colorama import Fore
import os

pyver = f"{sys.version[0]}{sys.version[1]}{sys.version[2]}{sys.version[3]}{sys.version[4]}{sys.version[5]}{sys.version[6]}"

help = f"""
Commands:

{Fore.LIGHTWHITE_EX}- cd [path] - {Fore.BLUE}Changes directory
{Fore.LIGHTWHITE_EX}- dir - {Fore.BLUE}Lists the items of the current directory
{Fore.LIGHTWHITE_EX}- help - {Fore.BLUE}Shows a help message
{Fore.LIGHTWHITE_EX}- exec [name] - {Fore.BLUE}Executes a file
{Fore.LIGHTWHITE_EX}- dfurl [url] [filesavename] - {Fore.BLUE}Downloads a file from the given url
{Fore.LIGHTWHITE_EX}- pycr - {Fore.BLUE}Opens Python code runner
"""

PyCodeRunnerInfo = f"""
Python Version : {pyver}"""

if __name__ == "__main__":
    dev = 0
    version = "0.0.1 Alpha"
    path = os.getcwd()
    print(f"{Fore.LIGHTWHITE_EX}Original PyConsole {version}\n"
          f"{Fore.LIGHTWHITE_EX}Made by VincTBest\n"
          f"{Fore.LIGHTWHITE_EX}Visit https://github.com/VincTBest/PyConsole to get the newes updates.\n")
    while True:
        command = input(f"{Fore.LIGHTWHITE_EX}{path}> ")
        tokens_space = command.split(" ")
        if tokens_space[0].lower() == "cd" and len(tokens_space) == 2:
            try:
                os.chdir(tokens_space[1])
                path = os.getcwd()
            except:
                print(f"{Fore.RED}ERROR: Can not change to a non-existing directory >> {tokens_space[1]} <<")
        elif tokens_space[0].lower() == "dir" and len(tokens_space) == 1:
            dir = os.listdir(os.getcwd())
            i = 0
            while i < len(dir):
                print(dir[i])
                i = i + 1
        elif tokens_space[0].lower() == "help" and len(tokens_space) == 1:
            print(help)
        elif tokens_space[0].lower() == "exec" and len(tokens_space) == 2:
            os.startfile(tokens_space[1])
        elif tokens_space[0].lower() == "dfurl" and len(tokens_space) == 3:
            import urllib.request
            s = urllib.request.urlopen(tokens_space[1]).read().decode()
            try:
                sf = open(file=tokens_space[2], mode="x")
                sf.write(s)
                sf.close()
                print(f"{Fore.LIGHTGREEN_EX}Successfully downloaded {tokens_space[2]} from {tokens_space[1]}")
            except:
                print(f"{Fore.RED}ERROR: There is already a file named >> {tokens_space[2]} <<")
        elif tokens_space[0].lower() == "pycr" and len(tokens_space) == 1:
            import customtkinter as ctk
            from CTkMenuBar import *
            from CTkMessagebox import *

            def runpycr():
                pycrcode = pycrinput.get("1.0", "999999999999999999999.0")
                print(f"{Fore.LIGHTWHITE_EX}PyCodeRunner : Python {pyver} >> {exec(pycrcode)}")

            def infopycr():

                CTkMessagebox(title="PyCommandRunner Info", message=PyCodeRunnerInfo,)

                # infopycrnew = ctk.CTkToplevel()
                # infopycrnew.geometry("400x300")
                # infopycrnew.title("PyCodeRunner Info")
                # infopycrnew_label = ctk.CTkLabel(infopycrnew, text=)

            def pycrrff():
                pycrrffdlg = ctk.CTkInputDialog(title="PyCR : RunFromFile", text="File Name:")
                pycrrffdlgin = pycrrffdlg.get_input()
                try:
                    pycrrffdlgfile = open(file=pycrrffdlgin, mode="r")
                    pycrrffdlgfileread = pycrrffdlgfile.read()
                    print(f"{Fore.LIGHTWHITE_EX}PyCodeRunner : Python {pyver} >> {pycrrffdlgfile}")
                    exec(pycrrffdlgfileread)
                    pycrrffdlgfile.close()
                except:
                    print(f"{Fore.RED}ERROR: Did not found Python file named >> {pycrrffdlgin} <<")

            pycoderunner = ctk.CTk()
            pycoderunner.geometry("560x380")
            pycoderunner.title("PyCodeRunner")

            pycrinput = ctk.CTkTextbox(pycoderunner, width=1920*4, height=2160*4)
            pycrinput.pack(padx=10, pady=10)

            menu = CTkTitleMenu(pycoderunner)
            ctmbtn = menu.add_cascade("Commands")

            ctmmenu = CustomDropdownMenu(widget=ctmbtn)
            ctmmenu.add_option(option="Run", command=runpycr)
            ctmmenu.add_option(option="Info", command=infopycr)
            ctmmenu.add_option(option="Run From File", command=pycrrff)
            ctmmenu.add_option(option="Exit", command=pycoderunner.quit)

            pycoderunner.mainloop()

        elif tokens_space[0].lower() == "qr" and len(tokens_space) == 4 and dev == 1:
            pass
            # if tokens_space[1].lower() == "make" and len(tokens_space) == 4:
            #     import qrcode
            #
            #     # Function to generate and display QR code
            #     def generate_qr_code(data, filename='qrcode.png'):
            #         # Create a QR Code object
            #         img = qrcode.make(data)
            #
            #         # Save the image to a file
            #         img.save(filename)
            #
            #         # Display the QR code image
            #         img.show()
            #
            #         print(f'QR code generated and saved as {filename}')
            #
            #     # Usage
            #     data = tokens_space[2]  # The data you want to encode in the QR code
            #     filename = tokens_space[3]  # The name of the file where the QR code will be saved
            #     generate_qr_code(data, filename)
            # elif tokens_space[1].lower() == "read" and len(tokens_space) == 3:
            #     pass
        elif tokens_space[0].lower() == "dev" and len(tokens_space) == 2:
            if tokens_space[1].lower() == "1":
                dev = 1
            elif tokens_space[1].lower() == "0":
                dev = 0
        else:
            try:
                os.startfile(tokens_space[0])
            except:
                print(f"{Fore.RED}ERROR: >> {tokens_space[0]} << is not a recognized command or executeable")
        print("")