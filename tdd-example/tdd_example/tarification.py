def get_price(age: int) -> int:
    if age == 0:
        return 0
    elif age ==18:
        raise Exception("L'age de la personne que vous avez rensigné, "
                        f"{age} ans, n'est pas compris entre 0 et 17 ans inclus.")
