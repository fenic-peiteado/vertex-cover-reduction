import sys
import json
import graph_visualization as gv

###########################
# Entrada/Salida del json #
###########################
def readInput(file):
  with open(file, 'r') as f:
    data = json.load(f)

  variables = data.get("variables")
  clausulas = data.get("clausulas")

  return [variables, clausulas]

def writeOutput(file, vc_structure):
  print(vc_structure)
  output = json.dumps(vc_structure, indent=2,separators=(',', ':',))
  print(output)
  with open(file, 'w') as f:
    f.write(output)


################## peiteado padilla + chatgpt = chateado ptdilla
# Transformación #
##################
def get_truth_settings(variables):
  vertex = []
  edges = []
  for var in variables:
    var1 = var
    var2 = "n_" + var
    vertex.append(var1)
    vertex.append(var2)
    edges.append([var1, var2])
  return [vertex, edges]

def get_satisfaction_testing(clausulas):
  vertex = []
  edges = []
  for clausula in range(1, len(clausulas) + 1):
    for termino in range(1, 4):
      vertex.append(f"c{clausula}_{termino}")

    edges.append([f"c{clausula}_1", f"c{clausula}_2"])
    edges.append([f"c{clausula}_1", f"c{clausula}_3"])
    edges.append([f"c{clausula}_2", f"c{clausula}_3"])
  return [vertex, edges]

def get_communication_edges(clausulas):
  edges = []
  for clausula in range(1, len(clausulas) + 1):
    for termino in range(1, 4):
      nombre_origen = vertex_name(clausulas, clausula, termino)
      nombre_destino = f"c{clausula}_{termino}"
      edges.append([nombre_origen, nombre_destino])
  return edges

def vertex_name(clausulas, clausula, termino):
  nombre_origen = clausulas[clausula - 1][termino - 1]["variable"]
  if (clausulas[clausula - 1][termino - 1]["esNegado"]):
    nombre_origen = f"n_{nombre_origen}"
  return nombre_origen

def transform(variables, clausulas):
  # obtener truth settings
  [TS_vertex, TS_edges] = get_truth_settings(variables)
  # obtener satisfaction testing 
  [ST_vertex, ST_edges] = get_satisfaction_testing(clausulas)
  # obtener communication edges 
  CE_edges = get_communication_edges(clausulas)
  return {
    "truth-settings": { "vertices": TS_vertex, "aristas": TS_edges },
    "satisfaction-testing": { "vertices": ST_vertex, "aristas": ST_edges },
    "communication-edges": { "aristas": CE_edges }
  }

###################################################
if len(sys.argv) != 3:
  sys.exit("Uso: python " + sys.argv[0] + "3SAT.json VC.json")

file_to_read = sys.argv[1]
file_to_write = sys.argv[2]

[variables, clausulas] = readInput(file_to_read)
output = transform(variables, clausulas)
writeOutput(file_to_write, output)
gv.PrintGraph(output)