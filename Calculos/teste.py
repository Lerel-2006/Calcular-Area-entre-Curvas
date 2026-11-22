from Funcoes import interpretar_funcao

resultado = interpretar_funcao("x**2 + 3*x")

print(resultado)

from Distancia import distacia

f = interpretar_funcao("x**2")
g = interpretar_funcao("x")

resultado = distacia(f, g)

print("Pontos de interseção: ", resultado)


from Integral import calcular_areas

areas = calcular_areas(f, g, resultado)

for area in areas:
    print("Intervalo:", area["inicio"], "até", area["fim"])
    print("Função superior:", area["superior"])
    print("Função inferior:", area["inferior"])
    print("Área:", area["area"])