def get_price(age: int) -> int:
    if age < 0:
        raise Exception(
            "L'âge de la personne que vous avez renseigné, "
            f"{age} ans, est négatif ! Ce n'est pas une valeur valide."
        )
    elif age <= 17:
        return 0
    else:
        raise Exception(
            "L'age de la personne que vous avez renseigné, "
            f"{age} ans, n'est pas compris entre 0 et 17 ans inclus."
        )
