import matplotlib.pyplot as plt

# Dados de exemplo (substitua pelos seus dados reais)
anos = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
medias_temperatura = [20.5, 21.2, 19.8, 22.0, 20.3, 21.8, 19.5, 20.7, 21.1, 20.9, 19.8]

# Crie o gráfico de barras
plt.figure(figsize=(8, 6))  # Tamanho da figura (opcional)

plt.bar(anos, medias_temperatura, color='skyblue', edgecolor='black')
plt.xlabel('Ano')
plt.ylabel('Média de temperatura mínima (°C)')
plt.title('Médias de temperatura mínima em agosto (2006-2016)')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Exiba o gráfico
plt.show()