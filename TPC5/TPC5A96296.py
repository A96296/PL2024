import json

class VendingMachine:
    def __init__(self):
        self.stock = []
        self.load_stock()
        self.balance = 0

    def load_stock(self):
        try:
            with open('stock.json', 'r') as file:
                self.stock = json.load(file)
            print("maq: Stock carregado, Estado atualizado.")
        except FileNotFoundError:
            print("maq: Não foi possível carregar o stock. Criando novo stock vazio.")
            self.stock = []

    def save_stock(self):
        with open('stock.json', 'w') as file:
            json.dump(self.stock, file)

    def display_stock(self):
        print("maq:")
        print("cod | nome | quantidade | preço")
        print("---------------------------------")
        for item in self.stock:
            print(f"{item['cod']} {item['nome']} {item['quant']} {item['preco']}")

    def process_coin(self, coins):
        for coin in coins:
            if coin.endswith('e'):
                self.balance += int(coin[:-1]) * 100
            elif coin.endswith('c'):
                self.balance += int(coin[:-1])

    def select_product(self, code):
        for item in self.stock:
            if item['cod'] == code:
                if item['quant'] > 0:
                    if self.balance >= item['preco'] * 100:
                        item['quant'] -= 1
                        self.balance -= int(item['preco'] * 100)
                        print(f"maq: Pode retirar o produto dispensado \"{item['nome']}\"")
                        print(f"maq: Saldo = {self.balance//100}e{self.balance%100}c")
                    else:
                        print(f"maq: Saldo insuficiente para satisfazer o seu pedido")
                        print(f"maq: Saldo = {self.balance//100}e{self.balance%100}c; Pedido = {item['preco']}e")
                else:
                    print("maq: Produto esgotado.")
                return
        print("maq: Produto não encontrado.")

    def return_change(self):
        coins = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}
        change = self.balance
        for value in sorted(coins.keys(), reverse=True):
            while change >= value:
                coins[value] += 1
                change -= value
        self.balance = 0
        return coins

    def run(self):
        print("maq: Bom dia. Estou disponível para atender o seu pedido.")
        while True:
            command = input(">> ").strip().split()
            if command[0] == "LISTAR":
                self.display_stock()
            elif command[0] == "MOEDA":
                self.process_coin(command[1:])
                print(f"maq: Saldo = {self.balance//100}e{self.balance%100}c")
            elif command[0] == "SELECIONAR":
                if len(command) == 2:
                    self.select_product(command[1])
                else:
                    print("maq: Comando inválido.")
            elif command[0] == "SAIR":
                if self.balance > 0:
                    change = self.return_change()
                    print("maq: Pode retirar o troco:", end=" ")
                    for coin, quantity in change.items():
                        if quantity > 0:
                            print(f"{quantity}x {coin}c", end=", ")
                    print()
                print("maq: Até à próxima")
                self.save_stock()
                break
            else:
                print("maq: Comando inválido.")


if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()
