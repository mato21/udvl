class Formula: 
    def __init__(self, subformulas):
        self.subformulas = subformulas

    def subf(self):
        return self.subformulas

    def toString(self):
        return ""

    def eval(self, i):
        return False


class Variable(Formula):
    def __init__(self, name):
        Formula.__init__(self, []) #premenna nema podformulu
        self.name = name

    def toString(self):
        return self.name

    def eval(self, i): #i je interpretacia
        return i[self.name]   #hodi excepion ak premenna nie je v i


class Negation(Formula):
    def __init__(self, formula):
        Formula.__init__(self, [formula])

    def originalFormula(self):
        return self.subf()[0]

    def toString(self):
        return '-' + self.originalFormula().toString()

    def eval(self, i):
        return not self.originalFormula.eval(i)


class Disjunction(Formula):
    def __init__(self, subformulas):
        Formula.__init__(self, [formula])

    def toString(self):
        for prem in self.subf():
            return '(' + '|'.join([prem.toString()]) + ')'

    def eval(self, i):
        for prem in self.subf():
            if prem.eval(i) is True:
                return True
        return False

class Conjunction(Formula):
    def __init__(self, subformulas):
        Formula.__init__(self, subformulas)

    def toString(self):
       for prem in self.subf():
            return '(' + '&'.join([prem.toString()]) + ')'

    def eval(self, i):
        for prem in self.subf():
            if prem.eval(i) is True:
                return True
        return False

class BinFormula(Formula): #pre lahsiu intrepretaciu
    def __init__(self, left, right, vz):
        Formula.__init__(self, [left, right])
        self.vz = vz

    def leftSide(self):
        return self.subf() [0]

    def rightSide(self):
        return self.subf() [1]

    def toString(self):
        return '(' + (self.leftSide().toString() + self.vr + self.rightSide().toString()) + ')'
    
    def eval(self, i):
        pass

class Implication(BinFormula):
    def __init__(self,left,right):
        BinFormula.__init__(self, left, right, '=>')
    
    def eval(self, i):
        return self.rightSide().eval(i) or (not self.leftSide().eval(i))


class Equivalence(BinFormula):
    def __init__(self,left,right):
        BinFormula.__init__(self, left, right, '<=>')

    def eval(self, i):
         return self.leftSide().eval(i) == self.rightSide().eval(i)    
