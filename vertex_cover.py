import sys
import json

####################
# Lectura del json #
####################
def readInput(file):
  with open(file, 'r') as f:
    data = json.load(f)

  variables = data.get("variables")
  clausulas = data.get("clausulas")

  return [variables, clausulas]


##################
# Transformación #
##################
def calcula_truth_settings(variables):
  vertices = []
  aristas = []
  for var in variables:
    var1 = var
    var2 = "n_" + var
    vertices.insert(len(vertices), var1)
    vertices.insert(len(vertices), var2)
    aristas.insert(len(aristas), [var1, var2])
  return [vertices, aristas]

def calcula_satisfaction_testing():
  vertices = []
  aristas = []
  for c in clausulas:
    
  return [vertices, aristas]

def transform(variables, clausulas):
  # obtener truth settings
  [TS_vertex, TS_edges] = calcula_truth_settings(variables)
  # obtener satisfaction testing 
  [ST_vertex, ST_edges] = calcula_satisfaction_testing()
  # obtener communication edges 

###################################################
if len(sys.argv) != 3:
  sys.exit("Uso: python " + sys.argv[0] + "3SAT.json VC.json")

file_to_read = sys.argv[1]
file_to_write = sys.argv[2]

[variables, clausulas] = readInput(file_to_read)
output = transform(variables, clausulas)
