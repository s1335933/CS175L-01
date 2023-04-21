#Aidan Moxham
#CS-175L-01
#Expense Pie Chart

import matplotlib.pyplot as plt

def expensePieChart():
    try:
        with open('expenses.txt', 'r') as f:
            data = {}
            for line in f:
                label, value = line.strip().split('\t')
                try:
                    data[label] = int(value)
                except ValueError:
                    print(f"Invalid value for '{label}' category: '{value}'")
                    continue
            
            fig, ax = plt.subplots()
            ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
            ax.set_title("Expenses Pie Chart")
            plt.show()
    except IOError:
        print("Error: Unable to read file 'expenses.txt'")

if __name__ == '__main__':
    expensePieChart()
