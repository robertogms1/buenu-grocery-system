# 📦 Módulo de gerenciamento de estoque para o Buenu Grocery System

# Importa o módulo 'json' da biblioteca padrão do Python, usado para salvar e carregar dados em formato JSON
import json

# Importa o módulo 'os' para verificar se o arquivo de dados existe no sistema
import os

# Caminho do arquivo onde o estoque será salvo (dentro da pasta 'data')
ARQUIVO_ESTOQUE = 'data/estoque.json'


# 🧩 Função que carrega o estoque do arquivo JSON (se existir), ou cria um dicionário vazio
def carregar_estoque():
    if os.path.exists(ARQUIVO_ESTOQUE):  # Verifica se o arquivo existe
        with open(ARQUIVO_ESTOQUE, 'r') as f:  # Abre o arquivo em modo leitura
            return json.load(f)  # Converte o conteúdo JSON para um dicionário Python
    return {}  # Retorna um dicionário vazio se o arquivo não existir


# 💾 Função que salva o estado atual do estoque em formato JSON
def salvar_estoque(estoque):
    with open(ARQUIVO_ESTOQUE, 'w') as f:  # Abre o arquivo em modo escrita
        json.dump(estoque, f, indent=4)  # Salva o dicionário no arquivo com indentação legível


# ➕ Função que adiciona um novo produto ou atualiza a quantidade de um existente
def adicionar_produto(estoque, codigo_barras, nome, preco, quantidade):
    if codigo_barras in estoque:  # Verifica se o código de barras já existe no estoque
        estoque[codigo_barras]['quantidade'] += quantidade  # Soma as unidades à quantidade atual
        print(f"📦 Produto já existente. Quantidade atualizada para {estoque[codigo_barras]['quantidade']}.")
    else:
        estoque[codigo_barras] = {  # Cria um novo item com as informações básicas
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }
        print("✅ Novo produto adicionado com sucesso.")
    salvar_estoque(estoque)  # Salva o estoque atualizado no arquivo


# 📋 Função que exibe todos os produtos cadastrados no estoque
def listar_produtos(estoque):
    print("\n📦 Produtos em estoque:")
    for cod_barras, info in estoque.items():  # Percorre todos os itens do dicionário
        print(f"{info['nome']} | R${info['preco']} | Qtd: {info['quantidade']} | 🧾 Código de Barras: {cod_barras}")


# 💰 Função que permite alterar o preço de um produto existente
def atualizar_preco(estoque, codigo_barras, novo_preco):
    if codigo_barras in estoque:  # Verifica se o produto está cadastrado
        preco_antigo = estoque[codigo_barras]['preco']  # Guarda o preço antigo
        estoque[codigo_barras]['preco'] = novo_preco  # Atualiza o valor do preço
        salvar_estoque(estoque)  # Salva a modificação no arquivo
        print(f"💰 Preço atualizado com sucesso: R${preco_antigo} → R${novo_preco}")
    else:
        print("⚠️ Produto não encontrado. Verifique o código de barras informado.")


# 🔧 Bloco de teste: executado somente quando o arquivo é executado diretamente
if __name__ == '__main__':
    est = carregar_estoque()  # Carrega o estoque do arquivo (ou cria vazio)

    # Adiciona um produto de teste
    #adicionar_produto(est, '7891234567890', 'Arroz 5kg', 25.90, 10)

    # Altera o preço desse produto
    #atualizar_preco(est, '7891234567890', 28.90)

    # Lista todos os produtos após a modificação
    #listar_produtos(est)