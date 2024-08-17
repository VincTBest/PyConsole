from colorama import Fore
import os

help = f"""
Commands:

{Fore.LIGHTWHITE_EX}- cd [path] - {Fore.BLUE}Changes directory
{Fore.LIGHTWHITE_EX}- dir - {Fore.BLUE}Lists the items of the current directory
{Fore.LIGHTWHITE_EX}- help - {Fore.BLUE}Shows a help message
{Fore.LIGHTWHITE_EX}- exec [name] - {Fore.BLUE}Executes a file
{Fore.LIGHTWHITE_EX}- dfurl [url] - {Fore.BLUE}Downloads a file from the given url


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
        elif tokens_space[0].lower() == "dfurl" and len(tokens_space) == 2:
            import urllib.request
            s = urllib.request.urlopen(tokens_space[1]).read().decode()
        else:
            try:
                os.startfile(tokens_space[0])
            except:
                print(f"{Fore.RED}ERROR: >> {tokens_space[0]} << is not a recognized command or executeable")
        print("")