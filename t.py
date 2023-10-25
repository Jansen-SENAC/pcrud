import sqlite3

def criar_tabela():
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cargo TEXT NOT NULL,
            salario REAL NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def criar_funcionario(nome, cargo, salario):
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO funcionarios (nome, cargo, salario) VALUES (?, ?, ?)", (nome, cargo, salario))
    conn.commit()
    conn.close()

def listar_funcionarios():
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM funcionarios")
    funcionarios = cursor.fetchall()

    if len(funcionarios) > 0:
        print("Lista de Funcionários:")
        for funcionario in funcionarios:
            print(f"ID: {funcionario[0]}")
            print(f"Nome: {funcionario[1]}")
            print(f"Cargo: {funcionario[2]}")
            print(f"Salário: {funcionario[3]}\n")
    else:
        print("Não há funcionários cadastrados.")

    conn.close()

def atualizar_funcionario(funcionario_id, nome, cargo, salario):
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE funcionarios SET nome = ?, cargo = ?, salario = ? WHERE id = ?", (nome, cargo, salario, funcionario_id))
    conn.commit()
    conn.close()

def excluir_funcionario(funcionario_id):
    conn = sqlite3.connect('funcionarios.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM funcionarios WHERE id = ?", (funcionario_id,))
    conn.commit()
    conn.close()

# Criar a tabela se não existir
criar_tabela()

# Exemplos de uso
criar_funcionario("João", "Desenvolvedor", 5000.0)
criar_funcionario("Maria", "Designer", 4500.0)

print("Funcionários após a criação:")
listar_funcionarios()

atualizar_funcionario(21, "André", "Analista de Dados", 18500.0)

print("\nFuncionários após a atualização:")
listar_funcionarios()

excluir_funcionario(10)

print("\nFuncionários após a exclusão:")
listar_funcionarios()
