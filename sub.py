import numpy as np
import matplotlib.pyplot as plt


def cal_coll_cut(mass):
    ratio = mass/4.31e6
    x = np.linspace(0, 0.9999, 100)
    y = np.log10(1-x) + np.log10(3e-4) + np.log10(np.sqrt(ratio))
    return x, y


def main():
    x = np.linspace(0, 0.9999, 100)
    y = np.log10(1-x) + np.log10(3e-4)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    # ax.set_yscale('log')
    plt.show()


if __name__ == "__main__":
    main()