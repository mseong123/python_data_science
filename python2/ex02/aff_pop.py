from matplotlib import pyplot as plt
from load_csv import load


def convert(df):
    """convert series data uniformly for plotting"""
    df = df.copy()
    for x in df.index:
        if df[x].find("M") != -1:
            df[x] = float(df[x].replace("M", ""))
        elif df[x].find("k") != -1:
            df[x] = float(df[x].replace("k", "")) / 1000
        elif df[x].find("B") != -1:
            df[x] = float(df[x].replace("B", "")) * 1000
    return df


def convert_ticks(plt):
    """convert ticks to labels"""
    return [str(int(x)) + "M" for x in plt.gca().get_yticks()]


def main():
    """main"""
    df = load("population_total.csv")
    if df is not None:
        discard_column = [i for i in df.columns if (int(i) > 2050)]
        df = df.drop(columns=discard_column)
        df1 = df.loc['Malaysia']
        df2 = df.loc['United States']
        df1 = convert(df1)
        df2 = convert(df2)
        plt.title("Population Projections")
        plt.ylabel("Population")
        plt.xlabel("Year")
        try:
            df1.plot(color='b')
            df2.plot(color='g')
        except Exception as e:
            print(f"{e}")
        newTicksLabel = convert_ticks(plt)
        plt.gca().set_yticks(plt.gca().get_yticks(), newTicksLabel)
        plt.legend(loc="lower right")
        try:
            plt.show()
        except BaseException:
            pass


if __name__ == "__main__":
    main()
