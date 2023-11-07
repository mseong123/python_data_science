from matplotlib import pyplot as plt
from load_csv import load


def main():
    """main"""
    df1 = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    df2 = load("life_expectancy_years.csv")
    if df1 is not None and df2 is not None:
        df1 = df1.loc[:, ['1900']].rename(columns={'1900':
                                                   'Gross Domestic Product'})
        df2 = df2.loc[:, ['1900']]
        df1['Life Expectancy'] = df2['1900']
        df1.plot.scatter(x="Gross Domestic Product", y="Life Expectancy",
                         logx=True)
        plt.title("1900")
        plt.ylabel("Life Expectancy")
        plt.xlabel("Gross Domestic Product")
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        try:
            plt.show()
        except BaseException:
            pass


if __name__ == "__main__":
    main()
