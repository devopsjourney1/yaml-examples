import yaml
import sys

#Makes the Output pretty
from rich.console import Console
console = Console()

if __name__ == '__main__':

    stream = open(sys.argv[1], 'r')
    dictionary = yaml.load(stream, Loader=yaml.FullLoader)
    for key, value in dictionary.items():
        #Using console print to make output pretty
        console.print(key + " : " + str(value))