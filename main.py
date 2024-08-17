from colorama import Fore
import os

help = f"""
Commands:

{Fore.LIGHTWHITE_EX}- cd [path] - {Fore.BLUE}Changes directory
{Fore.LIGHTWHITE_EX}- lsdi - {Fore.BLUE}Lists the items of the current directory
{Fore.LIGHTWHITE_EX}- help - {Fore.BLUE}Shows a help message
"""

if __name__ == "__main__":
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
        elif tokens_space[0].lower() == "lsdi" and len(tokens_space) == 1:
            dir = os.listdir(os.getcwd())
            i = 0
            while i < len(dir):
                print(dir[i])
                i = i + 1
        elif tokens_space[0].lower() == "help" and len(tokens_space) == 1:
            print(help)
        else:
            print(f"{Fore.RED}ERROR: >> {tokens_space[0]} << is not a recognized command or executeable")
        print("")