from matplotlib import pyplot as plt
from load_csv import load


def main():
    """main"""
    df = load("life_expectancy_years.csv")
    if df is not None:
        df = df.loc['Malaysia']
        plt.title("Malaysia Life expectancy Projections")
        plt.ylabel("Life Expectancy")
        plt.xlabel("Year")
        df.plot()
        try:
            plt.show()
        except BaseException:
            pass


if __name__ == "__main__":
    main()
