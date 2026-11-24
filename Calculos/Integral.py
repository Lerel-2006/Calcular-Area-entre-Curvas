import sympy as sp


def avaliar_funcao(funcao, x, ponto):

    valor = sp.N(funcao.subs(x, ponto))
#Sp.n tensforma em valor numercico
    if valor.is_real is not True or valor.is_finite is not True:
        raise ValueError(
            "Uma das funções não está definida em todo o intervalo."
        )

    return valor


def verificar_area(area):

    valor = sp.N(area)

    if valor.is_real is not True or valor.is_finite is not True:
        raise ValueError(
            "Não foi possível calcular uma área finita nesse intervalo."
        )


def calcular_areas(fx, gx, distancia):
    x = sp.Symbol("x")

    pontos = []

    for ponto in distancia:
        if ponto.is_real:
            pontos.append(ponto)

    pontos = sorted(set(pontos), key=lambda p: float(sp.N(p)))

    resultados = []

    for i in range(len(pontos) - 1):
        inicio = pontos[i]
        fim = pontos[i + 1]

        meio = (inicio + fim) / 2

        v1 = avaliar_funcao(fx, x, meio)
        v2 = avaliar_funcao(gx, x, meio)

        if v1 > v2:
            cima = fx
            baixo = gx
        else:
            baixo = fx
            cima = gx

        area = sp.integrate(
            cima - baixo,
            (x, inicio, fim)
        )

        verificar_area(area)

        resultados.append({
            "inicio": inicio,
            "fim": fim,
            "superior": cima,
            "inferior": baixo,
            "area": sp.simplify(area)
        })

    return resultados


def calcular_area_intervalo(fx, gx, inicio, fim):
    x = sp.Symbol("x")

    inicio = sp.sympify(inicio)
    fim = sp.sympify(fim)

    if not inicio.is_real or not fim.is_real:
        raise ValueError("Os limites precisam ser números reais.")

    if sp.N(inicio) >= sp.N(fim):
        raise ValueError(
            "O limite inicial precisa ser menor que o final."
        )

    diferenca = fx - gx

    pontos = [inicio, fim]

    intersecoes = sp.solveset(
        diferenca,
        x,
        domain=sp.Interval(inicio, fim)
    )

    if isinstance(intersecoes, sp.FiniteSet):
        for ponto in intersecoes:
            if ponto.is_real:
                pontos.append(ponto)

    pontos = sorted(set(pontos),key=lambda p: float(sp.N(p)))

    resultados = []

    for i in range(len(pontos) - 1):
        a = pontos[i]
        b = pontos[i + 1]

        meio = (a + b) / 2

        valor_fx = avaliar_funcao(fx, x, meio)
        valor_gx = avaliar_funcao(gx, x, meio)

        if valor_fx >= valor_gx:
            cima = fx
            baixo = gx
        else:
            cima = gx
            baixo = fx

        area = sp.integrate(
            cima - baixo,
            (x, a, b)
        )

        # Verifica se a área é válida
        verificar_area(area)

        resultados.append({
            "inicio": a,
            "fim": b,
            "superior": cima,
            "inferior": baixo,
            "area": sp.simplify(area)
        })
        

    return resultados


def calcular_integral_indefinida(fx, gx):
    x = sp.Symbol("x")

    integral_fx = sp.integrate(fx, x)
    integral_gx = sp.integrate(gx, x)

    return {
        "integral_fx": integral_fx,
        "integral_gx": integral_gx
    }