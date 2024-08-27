import tkinter as tk
from tkinter import messagebox
from collections import Counter

def produto_mais_vendido(produtos):
    contagem = Counter(produtos)
    max_produto = max(contagem, key=contagem.get)
    return max_produto

def processar_produtos():
    entrada = entrada_produtos.get()
    if entrada.strip():
        produtos = [produto.strip() for produto in entrada.split(',')]
        try:
            produto_mais_vendido_result = produto_mais_vendido(produtos)
            resultado_label.config(text=f'O produto mais vendido é: {produto_mais_vendido_result}')
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro: {e}")
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira produtos separados por vírgula.")

# Configuração da janela principal
root = tk.Tk()
root.title("Produto Mais Vendido")

# Label e Entry para entrada dos produtos
entrada_label = tk.Label(root, text="Insira produtos (separados por vírgula):")
entrada_label.pack(pady=20)
entrada_produtos = tk.Entry(root, width=100)
entrada_produtos.pack(pady=5)

# Botão para processar os produtos
processar_btn = tk.Button(root, text="Processar", command=processar_produtos)
processar_btn.pack(pady=10)

# Label para exibir o resultado
resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=10)

# Iniciar o loop da interface gráfica
root.mainloop()
