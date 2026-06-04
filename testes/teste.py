import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        I = int(entry_i.get())
        Ca = int(entry_ca.get())
        F = int(entry_f.get())
        A = int(entry_a.get())
        Co = int(entry_co.get())
        nivel = int(entry_nivel.get())

        N = nivel - 1
        

        mana = 20 + 5 * (I + Ca) + (10 * N)
        vida = 20 + (5 * Co) + (5 * N)
        stamina = 20 + 5 * (A + F) + (10 * N)
        Fr = 100 + ((I // 5) * 5 + (Ca // 5) * 5)

        rf = Co + F * 2
        rm = Co + I

        m = 3 + A
        am = 4 + I
        af = 1

        resultado.config(
            text=f"""
Mana: {mana}
Vida: {vida}
Stamina: {stamina}
Fio de Razão: {Fr}%

Res. Física: {rf}
Res. Mágica: {rm}

Movimentação: {m}
Alcance Mágico: {am}
Alcance Físico: {af}
"""
        )

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite apenas números!"
        )

janela = tk.Tk()
janela.title("Calculadora de Status RPG")
janela.geometry("500x600")

# Inteligência
tk.Label(janela, text="Inteligência").pack()
entry_i = tk.Entry(janela)
entry_i.pack()

# Carisma
tk.Label(janela, text="Carisma").pack()
entry_ca = tk.Entry(janela)
entry_ca.pack()

# Força
tk.Label(janela, text="Força").pack()
entry_f = tk.Entry(janela)
entry_f.pack()

# Agilidade
tk.Label(janela, text="Agilidade").pack()
entry_a = tk.Entry(janela)
entry_a.pack()

# Constituição
tk.Label(janela, text="Constituição").pack()
entry_co = tk.Entry(janela)
entry_co.pack()

# Nível
tk.Label(janela, text="Nível").pack()
entry_nivel = tk.Entry(janela)
entry_nivel.pack()

# Botão
tk.Button(
    janela,
    text="Calcular",
    command=calcular
).pack(pady=10)

resultado = tk.Label(
    janela,
    text="Os resultados aparecerão aqui.",
    justify="left"
)
resultado.pack()

janela.mainloop()