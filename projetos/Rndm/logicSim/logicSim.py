import tkinter
import numpy as np
import csv
import ast

truthTablesInput = []
truthTables = []
logicGates[] = 


#pega as tabelas verdade de um arquivo csv nomeado truthTables.csv que esteja no mesmo diretório que o programa, abre e trata os dados, assumindo que eles estão formatados da maneira correta
def loadTruthTables():
	#abre o arquivo e pega as truthtables no formato correto para uso
	with open("truthTables.txt") as csvFile:
		csvReader = csv.reader(csvFile, delimiter=" ")
		lineCount = 0
		#lê o arquivo e gera um array com as truthtables, mas na foramtação incorreta
		for row in csvReader:
			if lineCount == 0:
				lineCount += 1
			else:
				truthTablesInput.append(row)
				lineCount += 1

		#manipula as truthTablesInput de modo a formatar elas corretamente
		for row in truthTablesInput:
			row[1] = row[1].strip("[]").split(",")
			row[1] = [element.strip() for element in row[1]]
			row[2] = row[2].strip("[]").split(",")
			row[2] = [element.strip() for element in row[2]]
			truthTables.append(row)


class logicGate:
	"""Classe para os portões lógicos. possuem os parâmetros truthTable, nInputs, nOutputs, inputs, outputs, input, output """
	
	def __init__(self, name):
		super(logicGate, self).__init__()
		self.name = name
		self.truthTable = []
		for row in truthTables:
			if row[0] == self.name:
				self.truthTable.append(row[1])
				self.truthTable.append(row[2])

		self.inputs = self.truthTable[0]
		self.outputs = self.truthTable[1]
		self.nInputs = len(self.inputs)
		self.nOutputs = len(self.outputs)

		self._input = []
		self.output = []

	#looks at the input provided and evaluates the pertinet output
	def evaluate(self, _input):
		
		self.output = self.outputs[self.inputs.index(_input)]
		return(self.output)

	#gets the truth table pertinent to the logic gate name provided. funcionality already provided on the __init__() function, but here if needed!
	def getTruthTable(self):

		for row in truthTables:
			if row[0] == self.name:
				self.truthTable.append(row[1])
				self.truthTable.append(row[2])

		self.inputs = self.truthTable[0]
		self.outputs = self.truthTable[1]
		self.nInputs = len(self.inputs[0])
		self.nOutputs = len(self.outputs[0])

		return(self.inputs, self.outputs, self.nInputs, self.nOutputs)

	#inputs a logic gate into a global array
	def inputLogicGate():



def initialize():
	loadTruthTables()
	inputLogicGate()
