import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    x = np.arange(0, 6, 0.1)
    y = np.sin(x)

    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
