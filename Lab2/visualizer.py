import matplotlib.pyplot as plt

class DataVisualizer:
    @staticmethod
    def show_charts(data, counts):
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
        fig.suptitle('Wizualizacja danych')

        ax1.hist(data, bins='auto', color='skyblue', edgecolor='black')
        ax1.set_title('Histogram wartości')
        ax1.set_xlabel('Wartość')
        ax1.set_ylabel('Częstość')

        categories = ['Dodatnie', 'Ujemne', 'Zera']
        values = [counts['positive'], counts['negative'], counts['zeros']]
        ax2.bar(categories, values, color=['green', 'red', 'gray'])
        ax2.set_title('Struktura liczb')

        ax3.plot(data, marker='o', linestyle='-', color='purple')
        ax3.set_title('Kolejność wprowadzonych liczb')
        ax3.set_xlabel('Indeks')
        ax3.set_ylabel('Wartość')

        plt.tight_layout()
        plt.show()