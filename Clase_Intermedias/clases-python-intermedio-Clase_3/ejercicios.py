from collections import Counter

d = {
    "python": ["joaquin", "ana", "pedro"],  # 3
    "javascript": ["tomas"],  # 1
    "sql": []  # 0
}
l = [
    {"nombre": "joaquin", "lenguaje": "python"},
    {"nombre": "ana", "lenguaje": "python"},
    {"nombre": "pedro", "lenguaje": "python"},
    {"nombre": "tomas", "lenguaje": "javascript"},
]

c = Counter(persona["lenguaje"] for persona in l)
print(c)