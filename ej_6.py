import math

def max_rope_length(diametro, porcentage):
    radio = diametro / 2
    area = math.pi * (radio ** 2)
    allowed_area = area * porcentage
    max_length = 2 * math.pi * math.sqrt(allowed_area / math.pi)
    return int(max_length)
diameter = 50
percentage = 0.5
print("Longitud máxima de la cuerda:", max_rope_length(diameter, percentage), "pasos de ogro")
