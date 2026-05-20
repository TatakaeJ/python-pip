import csv


def read_csv(path):
    with open(path, "r") as filecsv:
        # Lee el archivo fila por fila
        reader = csv.reader(filecsv, delimiter=",")
        # Se obtiene la primera fila que es el encabezado de las columnas
        header = next(reader)
        data = []
        data_world_population = []
        for row in reader:
            # Une con tupla los pares del encabezado junto con el dato correspondiente a cada columna
            iterable = zip(header, row)
            # Obtiene la llave y el valor del iterable
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
            worl_population_dict = {
                key: value
                for key, value in country_dict.items()
                if key == "Country/Territory" or key == "World Population Percentage"
            }
            data_world_population.append(worl_population_dict)
        return data, data_world_population


if __name__ == "__main__":
    data, data_world_population = read_csv("./app/data.csv")
    print(data_world_population)
