# Formato de entrada. Problema 3-SAT.
```
{
  "variables": [
    "a",
    "b",
    "c",
    ...
  ]
  "clausulas": [ // Vector de conjunción de disyunciones
    [ // Vector de 3 objetos (disyunción)
      { // Descripción de cada elemento de la disyunción
        "esNegado": true,
        "variable": "a" // Debe estar en "variables"
      },
      {
        "esNegado": false,
        "variable": "c"
      },
      {
        "esNegado": true,
        "variable": "b"
      },
    ],
    ...
  ]
}
```
# Formato de salida. Problema VC.
```
{
  "truth-settings": {
    "vertices": ["a", "a2", ...],
    "aristas": [["a", "b"], ["a", "a2"], ...]
  },
  "satisfaction-testing": { 
    ...
  },
  "communication-edges": {
    "aristas": ... // En este caso solo nos interesan las aristas, los vértices ya han aparecido previamente
  }
}
```