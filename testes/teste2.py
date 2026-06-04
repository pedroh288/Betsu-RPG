import tkinter as tk
from tkinter import messagebox

def validar_int(valor):
    try:
        v = int(valor)
        if v <= 0:
            return None
        return v
    except:
        return None


def calcular():
    I = validar_int(entry_i.get())
    Ca = validar_int(entry_ca.get())
    F = validar_int(entry_f.get())
    A = validar_int(entry_a.get())
    Co = validar_int(entry_co.get())
    nivel = validar_int(entry_nivel.get())

    # bloqueia tudo se algum valor for inválido
    if None in (I, Ca, F, A, Co, nivel):
        messagebox.showerror(
            "Erro",
            "Todos os valores devem ser números MAIORES que zero!"
        )
        return

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

    resultado.config(text=f"""
Mana: {mana}
Vida: {vida}
Stamina: {stamina}
Fio de Razão: {Fr}%

Resistência Física: {rf}
Resistência Mágica: {rm}

Movimentação: {m}
Alcance Mágico: {am}
Alcance Físico: {af}
""")


janela = tk.Tk()
janela.title("Status RPG")
janela.geometry("500x600")

tk.Label(janela, text="Inteligência").pack()
entry_i = tk.Entry(janela)
entry_i.pack()

tk.Label(janela, text="Carisma").pack()
entry_ca = tk.Entry(janela)
entry_ca.pack()

tk.Label(janela, text="Força").pack()
entry_f = tk.Entry(janela)
entry_f.pack()

tk.Label(janela, text="Agilidade").pack()
entry_a = tk.Entry(janela)
entry_a.pack()

tk.Label(janela, text="Constituição").pack()
entry_co = tk.Entry(janela)
entry_co.pack()

tk.Label(janela, text="Nível").pack()
entry_nivel = tk.Entry(janela)
entry_nivel.pack()

tk.Button(janela, text="Calcular", command=calcular).pack(pady=10)

resultado = tk.Label(janela, text="", justify="left")
resultado.pack()

janela.mainloop()