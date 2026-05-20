def get_population(country_dict):
    population_dict = {
        "2022": int(country_dict["2022 Population"]),
        "2020": int(country_dict["2020 Population"]),
        "2015": int(country_dict["2015 Population"]),
        "2010": int(country_dict["2010 Population"]),
        "2000": int(country_dict["2000 Population"]),
        "1990": int(country_dict["1990 Population"]),
        "1980": int(country_dict["1980 Population"]),
        "1970": int(country_dict["1970 Population"]),
    }

    labels = population_dict.keys()
    values = population_dict.values()

    return labels, values


def get_world_pupulation_percentage(data_world_population):

    labels = [item["Country/Territory"] for item in data_world_population]
    values = [item["World Population Percentage"] for item in data_world_population]

    return labels, values


def get_population_by_country(data, country):
    """
    Resive la data (lista de diccionarios) y devuelve el que se le pide
    """
    result = list(filter(lambda item: item["Country/Territory"] == country, data))
    return result
