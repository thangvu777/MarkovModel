#################################################################################
# Author: Thang Vu                                                              #
# Version: 1.0                                                                  #
# Description: This program utilizes a Markov chain to generate English text    #
# that resembles characteristics of text files it has been trained on.          #
# This is because the Markov chain algorithm will decide the next most probable #
# surffix of a given order for a given prefix.                                  #
#################################################################################
# Language of choice: Python                                                    #
# Python has many useful libraries that can be used to build the statistical    #
# model used in the program such as numpy for multi-dimensional array           #
# computation as well as defaultdict, which is a high performance dictionary    #
# that does not raise key errors. Instead it provides the default value for a   #
# nonexistent key.                                                              #
#################################################################################

from Markov import Markov
# reads text file as one unified string
def readFile(source: str) -> str:
    try:
        with open (source) as file:
            array = file.readlines()
            return ''.join(array)
    except IOError:
        print("File could not be opened for reading.")

# writes output to a file
def writeFile(output: str, outFile: str) -> None:
    try:
        with open(outFile, "w") as file:
            file.write(output)
        print("The results have been exported as " + outFile)
    except IOError:
        print ("File could not be opened for writing.")

if __name__ == "__main__":
    # Prompt user for parameters
    order = int(input("Enter order: "))
    while (order <= 0):
        order = int(input("Invalid order\nEnter an order greater than 0: "))

    length = int(input("Enter desired length of sampled output: "))
    while (length <= 0):
        length = int(input("Invalid length\nEnter a length greater than 0: "))

    text = readFile(input("Enter name of local text file: "))
    outFileName = input("Enter name of output text file: ")

    # Create the model with text and order as parameters
    model = Markov(text, order)

    # If you wish to see the data dictionary
    # m.printdict(m.seqCollection)
    # m.printdict(m.tran)

    # one random sequence of length (order) that exists in the source text
    # this is the start of the seed
    randomSequence = model.randSeq(model.seqCollection)

    # You can also feed in the first sequence as well
    firstSeq = model.getFirstSeq(text,order)

    output = model.generateMarkovChain(randomSequence, length) # generate output with desired length
    writeFile(output, outFileName)  # write out the results

    # Exit code
    exit(0)
