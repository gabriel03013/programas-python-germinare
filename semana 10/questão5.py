def trocar_produtos(estoque):
    estoque_arrumado = {}
    for codigo, produto in estoque.items():
        estoque_arrumado[produto] = codigo

    return estoque_arrumado

estoque = {
    101: "Arroz",
    102: "Feijão",
    103: "Macarrão",
    104: "Açúcar",
    105: "Café",
    106: "Óleo",
    107: "Leite",
    108: "Farinha",
    109: "Sal",
    110: "Biscoito"
}

estoque2 = trocar_produtos(estoque)

for i in estoque2:
    print(f'{i} : {estoque2[i]}')
