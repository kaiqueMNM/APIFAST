#fast
#documentação
#assicromopip


from fastapi import FastAPI

app = FastAPI()
vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5, },
    2: {"item": "Garafa 2L", "preco_unitario": 5, "quantidade": 10,},
    3: {"item": "biscoito", "preco_unitario": 2, "quantidade": 100,},
    4: {"item": "arroz", "preco_unitario": 5, "quantidade": 7,},

}



@app.get("/")
def home():
    return {"vendas": len(vendas)}

@app.get("/vendas/{id_venda}")
def pegar_venda(id_venda: int):
    return vendas[id_venda]

    