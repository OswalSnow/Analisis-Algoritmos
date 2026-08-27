import tkinter as tk
import matplotlib.pyplot as plt

x = [0, 2, 4, 8]
y = [12, 48, 192, 768]
plt.plot(x,y)
plt.title("Grafica chida")
plt.scatter(x,y)
plt.xlabel("nombre del eje x")
plt.ylabel("nombre del eje y")

plt.show()


'''
def Salutations():
    name = entrada.get().strip()
    if not name:
        name = "no pusiste nada, q onda"
    lbl.config(text=f"Que rollo, {name}")

root = tk.Tk()
root.title("Saludador")
root.geometry("360x220")

lbl = tk.Label(root, text="Holaaa", background="purple4", foreground="gray")
lbl.pack(pady=20) 

entrada = tk.Entry(root)
entrada.pack(pady=25)

bot = tk.Button(root, text="Picale aqui", command=Salutations)
bot.pack(pady=30)

root.mainloop() # mainloop() siempre va al final
'''