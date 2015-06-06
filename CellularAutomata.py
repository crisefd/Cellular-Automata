#!/usr/bin/python3
#One Dimensional Cellular Automata
#Author: Cristhian Eduardo Fuertes Daza

#Class managing logic and computation of lattice's cells
class CellularAutomata():
    #Constructor
    #params:
    #numCells: the number of cells in each generation
    #rule_name: string representing the name of the rule to apply
    def __init__(self, numCells, rule_name):
        #List of rules
        self.__rules = [self.__rule30, self.__rule54, self.__rule60,
                        self.__rule62, self.__rule90, self.__rule94,
                        self.__rule102, self.__rule110, self.__rule122,
                        self.__rule126,self.__rule150, self.__rule158, 
                        self.__rule182, self.__rule188, self.__rule190,
                        self.__rule220, self.__rule222, self.__rule250]
        self.__numCells = numCells
        self.__rule_ind = self.__determinate_rule_ind(rule_name)
    
    #Uses the name of the rule to determinate the location in the 
    #rule's list     
    def __determinate_rule_ind(self, rule_name):
        if rule_name == "Rule 30":
            return 0
        elif rule_name == "Rule 54":
            return 1
        elif rule_name == "Rule 60":
            return 2
        elif rule_name == "Rule 62":
            return 3
        elif rule_name == "Rule 90":
            return 4
        elif rule_name == "Rule 94":
            return 5
        elif rule_name == "Rule 102":
            return 6
        elif rule_name == "Rule 110":
            return 7
        elif rule_name == "Rule 122":
            return 8
        elif rule_name == "Rule 126":
            return 9
        elif rule_name == "Rule 150":
            return 10
        elif rule_name == "Rule 158":
            return 11
        elif rule_name == "Rule 182":
            return 12
        elif rule_name == "Rule 188":
            return 13
        elif rule_name == "Rule 190":
            return 14
        elif rule_name == "Rule 220":
            return 15
        elif rule_name == "Rule 222":
            return 16
        elif rule_name == "Rule 250":
            return 17
        
    #Applies corresponding rule to the cells
    #param:
    #cell_list -> list of cells to apply rule
    #matrix -> 2-dimensional array representing the lattice
    #lattice -> lattice of button cells
    #generation -> the current generation
    def apply_rule(self, cell_list, matrix, lattice, generation):
        rule = self.__rules[self.__rule_ind]
        for k in range(0, len(cell_list)):
            cellpos = cell_list[k]
            rule(matrix, lattice, cellpos, generation)

    
    def __rule250(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule122(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule222(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule110(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule220(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule102(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule190(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule94(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule188(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule90(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule182(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule62(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule158(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule60(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule150(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
    
    def __rule54(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                
    
    
    def __rule126(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                #print(1)
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(2)
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               # print(3)

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(4)
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(5)

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(6)

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                #print(7)

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                
        

    def __rule30(self, matrix, lattice, cellPos, generation):
        if matrix[generation][cellPos] == 1:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                
            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                
            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               

            else:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                
        elif matrix[generation][cellPos] == 0:
            if matrix[generation][cellPos - 1] == 1 and matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                

            elif matrix[generation][cellPos - 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
                

            elif matrix[generation][cellPos + 1] == 1:
                matrix[generation + 1][cellPos] = 1
                lattice.get_child_at(cellPos, generation + 1).set_opacity(0.0)
               

            else:
                matrix[generation + 1][cellPos] = 0
                lattice.get_child_at(cellPos, generation + 1).set_opacity(1.0)
                
                