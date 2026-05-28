import charts as charts
import pandas as pd
import read_csv as read_csv
import utils as utils


def run():
    data, data_world_population = read_csv.read_csv("data.csv")

    option = int(
        input(
            "Elige una opción:\n1. Gráfico de barrar con el crecimiento de población en un país en especifico\n2. Gráfico de torta de los porcentajes de población de cada país"
        )
    )

    if option == 1:
        country = input("Ingresa un país: ")
        result = utils.get_population_by_country(data, country)

        if len(result) > 0:
            country = result[0]
            print(country)
            labels, values = utils.get_population(country)
            charts.generate_bar_chart(country["Country/Territory"], labels, values)
        else:
            print("El país no existe")
    elif option == 2:
        # dataframes (df) - todos los datos de donde obtienen los datos
        df = pd.read_csv("data.csv")
        # Filtrar por continente con pandas
        continent = input("Ingresa el nombre del continente: ")
        df = df[df["Continent"] == continent]
        # Labels y values del grafico optenidos con pandas
        countries = df["Country/Territory"].values
        percentages = df["World Population Percentage"].values

        # labels, values = utils.get_world_pupulation_percentage(data_world_population)
        charts.generate_pie_chart(continent, countries, percentages)


# hace que se ejecute como un script
if __name__ == "__main__":
    run()
