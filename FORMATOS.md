# Formato de entrada. Problema 3-SAT.
```json
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
```json
{
  "vertices": ["a", "a2", ...],
  "aristas": [["a", "b"], ["a", "a2"], ...]
}
```