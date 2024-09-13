import tkinter as tk
from tkinter import ttk
from datetime import datetime
import random

# Definir a classe do plano de voo
class FlightPlanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AeroStar Airlines - Plano de Voo")
        self.root.geometry("800x600")  # Aumentar o tamanho da janela para suportar mais voos

        # Tabela para mostrar as informações dos voos
        self.tree = ttk.Treeview(root, columns=("Número", "Destino", "País", "Horário", "Status"), show='headings', height=12)
        self.tree.heading("Número", text="Número do Voo")
        self.tree.heading("Destino", text="Destino")
        self.tree.heading("País", text="País")
        self.tree.heading("Horário", text="Horário")
        self.tree.heading("Status", text="Status")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Definir a largura das colunas para ajustar o texto
        self.tree.column("Número", width=100)
        self.tree.column("Destino", width=150)
        self.tree.column("País", width=100)
        self.tree.column("Horário", width=100)
        self.tree.column("Status", width=120)

        # Lista de 50 países e cidades fictícias da América do Sul
        self.cities = [
            ("São Paulo", "Brasil"), ("Rio de Janeiro", "Brasil"),
            ("Buenos Aires", "Argentina"), ("Santiago", "Chile"),
            ("Lima", "Peru"), ("Bogotá", "Colômbia"),
            ("Quito", "Equador"), ("La Paz", "Bolívia"),
            ("Montevidéu", "Uruguai"), ("Assunção", "Paraguai"),
            ("Caracas", "Venezuela"), ("Guayaquil", "Equador"),
            ("Cali", "Colômbia"), ("Córdoba", "Argentina"),
            ("Medellín", "Colômbia"), ("Rosário", "Argentina"),
            ("Valparaíso", "Chile"), ("Salvador", "Brasil"),
            ("Brasília", "Brasil"), ("Bariloche", "Argentina"),
            ("Cusco", "Peru"), ("Punta del Este", "Uruguai"),
            ("Mendoza", "Argentina"), ("Mar del Plata", "Argentina"),
            ("Fortaleza", "Brasil"), ("Florianópolis", "Brasil"),
            ("Manaus", "Brasil"), ("Recife", "Brasil"),
            ("Natal", "Brasil"), ("Belém", "Brasil"),
            ("Porto Alegre", "Brasil"), ("Vitória", "Brasil"),
            ("Iquique", "Chile"), ("Temuco", "Chile"),
            ("Antofagasta", "Chile"), ("Arequipa", "Peru"),
            ("Trujillo", "Peru"), ("Cuenca", "Equador"),
            ("Santa Cruz", "Bolívia"), ("Sucre", "Bolívia"),
            ("Manágua", "Nicarágua"), ("San José", "Costa Rica"),
            ("Cidade do Panamá", "Panamá"), ("Monte Cristi", "República Dominicana"),
            ("Cochabamba", "Bolívia"), ("Puerto Montt", "Chile"),
            ("Arica", "Chile"), ("Paramaribo", "Suriname"),
            ("Pucallpa", "Peru"), ("Ribeirão Preto", "Brasil")
        ]

        # Adicionar 12 voos fictícios no início
        for i in range(12):
            flight_num = f"AST{i+1:03d}"
            city, country = random.choice(self.cities)
            time = f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"
            status = random.choice(["No horário", "Atrasado", "Decolando", "Aterrissando"])
            self.add_flight(flight_num, city, country, time, status)

        # Iniciar atualização automática após 10 segundos
        self.update_time()

    # Método para adicionar um voo
    def add_flight(self, number, destination, country, time, status):
        self.tree.insert('', 'end', values=(number, destination, country, time, status))

    # Método para atualizar o horário e os dados do voo automaticamente a cada 10 segundos
    def update_time(self):
        for item in self.tree.get_children():
            current_time = datetime.now().strftime("%H:%M")
            new_city, new_country = random.choice(self.cities)  # Escolhe cidade e país aleatoriamente
            status = random.choice(["No horário", "Atrasado", "Decolando", "Aterrissando"])  # Atualiza o status aleatoriamente

            # Atualiza os valores na tabela
            self.tree.set(item, column="Destino", value=new_city)
            self.tree.set(item, column="País", value=new_country)
            self.tree.set(item, column="Horário", value=current_time)
            self.tree.set(item, column="Status", value=status)

        # Chama novamente a função após 10 segundos (10.000 milissegundos)
        self.root.after(10000, self.update_time)

# Criação da janela principal
if __name__ == "__main__":
    root = tk.Tk()
    app = FlightPlanApp(root)
    root.mainloop()
