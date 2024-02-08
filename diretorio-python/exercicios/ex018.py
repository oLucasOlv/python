import math

angulo = int(input('qual o ângulo: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'Seno de {angulo}° ≈  {seno:.4f}, Cosseno ≈  {cos:.4f}  Tangente ≈ {tan:.4f}')