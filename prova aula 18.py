import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "39076488894",
    "database": "sistema_vendas"
    }

class SistemaVendas:
    def __init__(self):
        self.conexao = mysql.connector.connect(**db_config)
        self.cursor = self.conexao.cursor()
        print("Conexão com o banco de dados estabelecida.")
    
    def cadastrar_produto(self, nome, descricao, qtd_disponivel, preco):
        sql = "INSERT INTO produtos (nome, descricao, qtd_disponivel, preco) VALUES (%s, %s, %s, %s)"
        valores = (nome, descricao, qtd_disponivel, preco)
        self.cursor.execute(sql, valores)
        self.conexao.commit()
        print(f"Produto '{nome}' cadastrado com sucesso!")

    def listar_produtos(self):
        janela = "SELECT nome, descricao, qtd_disponivel, preco FROM produtos"
        self.cursor.execute(janela)
        produtos = self.cursor.fetchall()
        if not produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("Produtos cadastrados:")
            for produto in produtos:
                print(f"Nome: {produto[0]}, Descrição: {produto[1]}, qtd_disponivel: {produto[2]}, Preço: {produto[3]}")
    
    def atualizar_quantidade(self, nome, nova_quantidade):
        janela = "UPDATE produtos SET qtd_disponivel = %s WHERE nome = %s"
        valores = (nova_quantidade, nome)
        self.cursor.execute(janela, valores)
        self.conexao.commit()
        if self.cursor.rowcount > 0:
            print(f"Quantidade do produto '{nome}' atualizada para {nova_quantidade}.")
        else:
            print(f"Produto '{nome}' não encontrado.")

    def remover_produto(self, nome):
        janela = "DELETE FROM produtos WHERE nome = %s"
        valores = (nome,)
        self.cursor.execute(janela, valores)
        self.conexao.commit()
        if self.cursor.rowcount > 0:
            print(f"Produto '{nome}' removido com sucesso!")
        else:
            print(f"Produto '{nome}' não encontrado.")

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
        print("Conexão com o banco de dados encerrada.")

def main():
    sistema_de_vendas = SistemaVendas()
    
    while True:
        print("Escolha uma opção:")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Atualizar Quantidade de Produto")
        print("4. Remover Produto")
        print("5. Sair")
        
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            descricao = input("Digite a descrição do produto: ")
            qtd_disponivel = int(input("Digite a quantidade disponível: "))
            preco = float(input("Digite o preço do produto: "))
            sistema_de_vendas.cadastrar_produto(nome, descricao, qtd_disponivel, preco)
        
        elif opcao == "2":
            sistema_de_vendas.listar_produtos()
        
        elif opcao == "3":
            nome = input("Digite o nome do produto para atualizar a quantidade: ")
            nova_quantidade = int(input("Digite a nova quantidade: "))
            sistema_de_vendas.atualizar_quantidade(nome, nova_quantidade)
        
        elif opcao == "4":
            nome = input("Digite o nome do produto para remover: ")
            sistema_de_vendas.remover_produto(nome)
        
        elif opcao == "5":
            print("Saindo do sistema...")
            sistema_de_vendas.fechar_conexao()
            break
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
