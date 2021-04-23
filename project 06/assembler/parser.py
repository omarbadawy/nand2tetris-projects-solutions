class Parser:
    def __init__(self):
        pass

    def instructionType(self, ins):
        if ins[0] == "@":
            return "A_instruction"
        elif ins[0] == "(":
            return "L_instruction"
        else:
            return "C_instruction"

    def symbol(self, ins):
        return ins[1:]

    def getDest(self, ins):
        ind = ins.find("=")

        if ind != -1:
            return ins[:ind]
        else:
            return "null"

    def getComp(self, ins):
        ind1 = ins.find("=")
        ind2 = ins.find(";")

        if ind1 != -1 and ind2 != -1:
            return ins[ind1 + 1 : ind2]
        elif ind1 != -1 and ind2 == -1:
            return ins[ind1 + 1 :]
        elif ind1 == -1 and ind2 != -1:
            return ins[:ind2]
        elif ind1 == -1 and ind2 == -1:
            return ins

    def getJump(self, ins):
        ind = ins.find(";")

        if ind != -1:
            return ins[ind + 1 :]
        else:
            return "null"
