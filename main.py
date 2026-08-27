import math
import matplotlib.pyplot as plt

# ==============================
# ENTRADA DE DADOS
# ==============================

quantidade = int(input("Quantos produtos você pretende comprar? "))

custo = float(input("Qual o custo de cada produto (R$)? "))

preco_venda = float(
    input("Por quanto você pretende vender cada produto (R$)? ")
)

chance_venda = float(
    input("Qual a chance de vender cada produto (%): ")
)


# ==============================
# CÁLCULOS
# ==============================

p = chance_venda / 100
q = 1 - p

investimento = quantidade * custo

# Lista para o gráfico
lucros = []
probabilidades = []

prob_lucro = 0
prob_prejuizo = 0
lucro_esperado = 0


# ==============================
# DISTRIBUIÇÃO BINOMIAL
# ==============================

for vendidos in range(quantidade + 1):

    # Probabilidade de vender exatamente
    # essa quantidade de produtos
    probabilidade = (
        math.comb(quantidade, vendidos)
        * (p ** vendidos)
        * (q ** (quantidade - vendidos))
    )

    # Resultado financeiro
    receita = vendidos * preco_venda
    lucro = receita - investimento

    # Guarda para o gráfico
    lucros.append(lucro)
    probabilidades.append(probabilidade * 100)

    # Lucro esperado
    lucro_esperado += lucro * probabilidade

    # Probabilidade de lucro/prejuízo
    if lucro > 0:
        prob_lucro += probabilidade

    elif lucro < 0:
        prob_prejuizo += probabilidade


# ==============================
# PONTO DE EQUILÍBRIO
# ==============================

if preco_venda > 0:
    ponto_equilibrio = math.ceil(investimento / preco_venda)
else:
    ponto_equilibrio = None


# ==============================
# RESULTADOS
# ==============================

print("\n========================================")
print("              RESULTADO")
print("========================================")

print(f"Produtos comprados:       {quantidade}")
print(f"Custo por produto:        R$ {custo:.2f}")
print(f"Preço de venda:           R$ {preco_venda:.2f}")
print(f"Investimento total:       R$ {investimento:.2f}")

print(f"\nChance de venda:          {chance_venda:.2f}%")
print(f"Chance de não vender:     {100 - chance_venda:.2f}%")

if ponto_equilibrio is not None:
    print(f"\nPonto de equilíbrio:      {ponto_equilibrio} produtos")

print("\n----------------------------------------")

print(f"Chance de ter LUCRO:      {prob_lucro * 100:.2f}%")
print(f"Chance de ter PREJUÍZO:   {prob_prejuizo * 100:.2f}%")

print(f"\nLucro esperado:           R$ {lucro_esperado:.2f}")

print("========================================")


# ==============================
# GRÁFICO
# ==============================

plt.figure(figsize=(11, 6))

plt.plot(
    lucros,
    probabilidades,
    marker="o",
    markersize=3,
    linewidth=1.5
)

# Linha horizontal no zero de probabilidade
plt.axhline(
    0,
    linestyle="--"
)

# Linha vertical em R$ 0
plt.axvline(
    0,
    linestyle="--",
    label="R$ 0 (ponto entre prejuízo e lucro)"
)

plt.xlabel("Lucro / Prejuízo (R$)")

plt.ylabel("Probabilidade (%)")

plt.title(
    "Distribuição da Probabilidade de Lucro ou Prejuízo"
)

plt.legend()

plt.grid(True, alpha=0.3)

plt.tight_layout()

plt.show()