import matplotlib.pyplot as plt
import numpy as np

def plot_data():
    labels = ['Car', 'Bike']
    booked = [50, 30]
    not_booked = [20, 40]

    x = np.arange(len(labels))

    plt.bar(x, booked, label='Booked')
    plt.bar(x, not_booked, bottom=booked, label='Not Booked')

    plt.xticks(x, labels)
    plt.title("Vehicle Booking Distribution")
    plt.legend()
    plt.show()