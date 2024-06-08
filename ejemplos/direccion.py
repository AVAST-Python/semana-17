data = {
  "game": { },
  "turn": 3,
  "board": {
    "height": 11,
    "width": 11,
    # ...
  },
  "you": {
    # ...
    "body": [
      { "x": 3, "y": 6 },
      { "x": 3, "y": 5 },
      { "x": 2, "y": 5 }
    ],
    "head": { "x": 3, "y": 6 },
    "length": 3,
    # ...
  }
}

# Calculamos la dirección de la serpiente
def direccion(data):
    # Obtenemos la posición de la cabeza y la cola
    cabeza = data["you"]["head"]
    siguiente = data["you"]["body"][1]
    # Calculamos la dirección de la serpiente
    if cabeza["x"] > siguiente["x"]:
        return "left"
    if cabeza["x"] < siguiente["x"]:
        return "right"
    if cabeza["y"] > siguiente["y"]:
        return "up"
    return "down"


