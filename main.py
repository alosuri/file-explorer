import sys, os

class FileExplorer:
    def __init__(self):
        ...
    def listFile(self):
        for x in os.listdir(os.getcwd()):
            if os.path.isfile(x):
                print(f"{bcolors.HEADER}{bcolors.BOLD}{x}{bcolors.ENDC}", end=' ')
            else:
                print(f"{bcolors.OKGREEN}{bcolors.BOLD}{x}{bcolors.ENDC}", end=' ')

    def createFile(self, filename: str):
        with open(os.path.join(os.getcwd(), filename), 'w') as file:
            pass
        
    def help(self, command: str | None):
        match command:
            case "all":
                print("agasgdsgs")
            case _:
                print("No command found!")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if __name__ == "__main__":
    explorer: FileExplorer = FileExplorer()
    try:
        option: str = sys.argv[1]
        match option:
            case "list":
                explorer.listFile()
            case "create":
                if len(sys.argv) > 2:
                    explorer.createFile(sys.argv[2])
                else:
                    print("Provide filename!")
            case "help":
                if len(sys.argv) > 2:
                    explorer.help(sys.argv[2])
                else:
                    explorer.help("all")

    except IndexError as e:
        print(f"{bcolors.FAIL}Error: No arguments provided. Check {bcolors.BOLD}help{bcolors.ENDC}{bcolors.FAIL} command for more information.{bcolors.ENDC} \n{e}")