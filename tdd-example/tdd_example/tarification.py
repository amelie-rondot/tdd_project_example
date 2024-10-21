def get_price(age: int) -> int:
    if 0 <= age <= 17:
        return 0
    else:
        if age < 0:
            detail_error_message = "est négatif ! Ce n'est pas une valeur valide."
        else:
            detail_error_message = "n'est pas compris entre 0 et 17 ans inclus."
        error_message = (
            "L'âge de la personne que vous avez renseigné, "
            f"{age} ans, {detail_error_message}"
        )
        raise Exception(error_message)
