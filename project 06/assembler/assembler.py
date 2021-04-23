from parser import Parser
from code import Code
from symbolTable import SymbolTable
import sys


class Assembler:
    def __init__(self, path):
        self.parser = Parser()
        self.code = Code()
        self.symbolTable = SymbolTable()
        self.fileInAsm = open(path, "r")

    def binary(self, s):
        bin_symbol = "{0:b}".format(int(s))
        return "0" * (16 - len(bin_symbol)) + bin_symbol

    def firstPass(self):
        counter = 0
        for line in self.fileInAsm:
            if "//" in line:
                line = line[: line.find("//")]
            instruction = line.strip()

            if instruction == "":
                continue
            elif instruction.startswith("/"):
                continue

            instructionType = self.parser.instructionType(instruction)

            if instructionType == "L_instruction":
                label = instruction[instruction.find("(") + 1 : instruction.find(")")]
                self.symbolTable.addEntry(label, counter)
            elif instructionType in [
                "A_instruction",
                "C_instruction",
            ]:
                counter += 1

    def secondPass(self):
        self.fileInAsm.seek(0)
        ram_address = 16
        for line in self.fileInAsm:
            if "//" in line:
                line = line[: line.find("//")]
            instruction = line.strip()

            if instruction == "":
                continue
            elif instruction.startswith("/"):
                continue

            instructionType = self.parser.instructionType(instruction)

            if instructionType == "A_instruction":
                symbol = self.parser.symbol(instruction)

                if not symbol.isdigit() and not self.symbolTable.contains(symbol):
                    self.symbolTable.addEntry(symbol, ram_address)
                    ram_address += 1

    def generateCode(self):
        writeFile = (self.fileInAsm.name)[:-4]
        self.fileInHack = open(writeFile + "2.hack", "w")

        self.fileInAsm.seek(0)
        outputString = ""
        for line in self.fileInAsm:
            if "//" in line:
                line = line[: line.find("//")]
            instruction = line.strip()

            if instruction == "":
                continue
            elif instruction.startswith("/"):
                continue

            instructionType = self.parser.instructionType(instruction)
            if instructionType == "A_instruction":
                symbol = self.parser.symbol(instruction)
                if symbol.isdigit():
                    binaryNumber = self.binary(symbol)
                else:
                    binaryNumber = self.binary(self.symbolTable.getAddress(symbol))
                outputString += binaryNumber + "\n"

            elif instructionType == "C_instruction":
                dest = self.parser.getDest(instruction)
                comp = self.parser.getComp(instruction)
                jump = self.parser.getJump(instruction)

                ddd = self.code.dest(dest)
                ccccccc = self.code.comp(comp)
                jjj = self.code.jump(jump)

                outputString += "111" + ccccccc + ddd + jjj + "\n"

        self.fileInHack.write(outputString)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        assembler = Assembler(sys.argv[1])
        assembler.firstPass()
        assembler.secondPass()
        assembler.generateCode()
