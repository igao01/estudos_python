import pprint

films_dict = {
    "Vingadores":{
        "yearRelease": 2020,
        "imdbRating": 9.5,
        "genre": ["Sci-fi", "Action", "Heroes"]
    },
    "As Branquelas":{
            "yearRelease": 2006,
            "imdbRating": 9.3,
            "genre": ["Comedy", "Action"]
        },
    "Mad Max":{
            "yearRelease": 2020,
            "imdbRating": 8.2,
            "genre": ["Sci-fi", "Action"]
        }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(films_dict)

# 1 - Buscar uma informação no dicionario aninhado
print(films_dict["As Branquelas"]["genre"])

# 2 - Adicionar um novo item
films_dict["Mad Max"]["director"] = "Tom holand"
pp.pprint(films_dict["Mad Max"])

# 3 - Deletar um item do dicionario
del films_dict["Mad Max"]
pp.pprint(films_dict)