import sys

class CellularAutomata():

    def __init__(self, numCells, rule_ind):
        #super(CellularAutomata, self).__init__()
        self.__rules = [self.__rule1]
        self.__numCells = numCells
        self.__rule_ind = rule_ind

    def applyRule(self, matrix, lattice, generation):
        print('applying rule')
        rule = self.__rules[self.__rule_ind]
        for cellPos in (1, self.__numCells - 1):
            #try:
             rule(matrix, lattice, cellPos, generation)
            #except:
             #   print('generation: ', generation, 'cellPos: ', cellPos)
              #  sys.exit(1)

        return matrix

    def __rule1(self, matrix, lattice, cellPos, generation):
        if matrix[cellPos][generation] == 1:
            if matrix[cellPos - 1][generation] == 1 and matrix[cellPos + 1][generation] == 1:
                matrix[cellPos][generation + 1] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
            elif matrix[cellPos - 1][generation] == 1:
                matrix[cellPos][generation + 1] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
            elif matrix[cellPos + 1][generation] == 1:
                matrix[cellPos][generation + 1] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)

            else:
                matrix[cellPos][generation + 1] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
        elif matrix[cellPos][generation] == 0:
            if matrix[cellPos - 1][generation] == 1 and matrix[cellPos + 1][generation] == 1:
                matrix[cellPos][generation + 1] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)

            elif matrix[cellPos - 1][generation] == 1:
                matrix[cellPos][generation + 1] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)

            elif matrix[cellPos + 1][generation] == 1:
                matrix[cellPos][generation + 1] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)

            else:
                matrix[cellPos][generation + 1] = 0
                try:
                    lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                except:
                    print('XXXX generation:', (generation + 1), 'cellPos: ', cellPos)
                    sys.exit(1)