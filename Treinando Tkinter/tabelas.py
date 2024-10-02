from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

janela = Tk()
janela.title("Graficos")
janela.geometry("600x400")

#Crinado figura nova
figura = plt.Figure(figsize=(8,4), dpi=60)
ax = figura.add_subplot(111)

canva = FigureCanvasTkAgg(figura, janela)
canva.get_tk_widget().grid(column=0, row=0)



fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')


janela.mainloop()
