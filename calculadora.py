import tkinter as tk

ventana = tk.Tk()
ventana.title("Calculadora")

# ■ .frame = contenedor para los botones
contenedor1 = tk.Frame(ventana)
contenedor1.pack()

tk.Button(contenedor1, text="7").pack(side=tk.LEFT)
tk.Button(contenedor1, text="8").pack(side=tk.LEFT)
tk.Button(contenedor1, text="9").pack(side=tk.LEFT)
tk.Button(contenedor1, text="/").pack(side=tk.LEFT)

contenedor2 = tk.Frame(ventana)
contenedor2.pack()
tk.Button(contenedor2, text="4").pack(side=tk.LEFT)
tk.Button(contenedor2, text="5").pack(side=tk.LEFT)
tk.Button(contenedor2, text="6").pack(side=tk.LEFT)
tk.Button(contenedor2, text="*").pack(side=tk.LEFT)

contenedor3 = tk.Frame(ventana)
contenedor3.pack()
tk.Button(contenedor3, text="1").pack(side=tk.LEFT)
tk.Button(contenedor3, text="2").pack(side=tk.LEFT)
tk.Button(contenedor3, text="3").pack(side=tk.LEFT)
tk.Button(contenedor3, text="-").pack(side=tk.LEFT)

contenedor4 = tk.Frame(ventana)
contenedor4.pack()
tk.Button(contenedor4, text="0").pack(side=tk.LEFT)
tk.Button(contenedor4, text=".").pack(side=tk.LEFT)
tk.Button(contenedor4, text="=").pack(side=tk.LEFT)
tk.Button(contenedor4, text="+").pack(side=tk.LEFT)

fila5 = tk.Frame(ventana)
fila5.pack()
tk.Button(fila5, text="C").pack()

ventana.mainloop()
