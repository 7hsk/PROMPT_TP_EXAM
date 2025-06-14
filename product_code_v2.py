def format_product_code(product_id: str) -> str:
    """
    Formate un code produit en insérant des tirets aux positions spécifiées.
    
    Args:
        product_id (str): Code produit à formater. Doit être une chaîne de 10 caractères
                         alphanumériques.
    
    Returns:
        str: Code produit formaté avec des tirets après le 3ème et le 6ème caractère.
             Format: XXX-XXX-XXXX
    
    Raises:
        ValueError: Si le code produit n'a pas exactement 10 caractères
                   ou contient des caractères non alphanumériques.
    
    Examples:
        >>> format_product_code("ABC123DEF4")
        'ABC-123-DEF4'
        >>> format_product_code("XYZ987GHIJ")
        'XYZ-987-GHIJ'
        >>> format_product_code("SHORT")
        Traceback (most recent call last):
        ...
        ValueError: Le code produit doit contenir exactement 10 caractères
    """
    # Vérification de la longueur
    if len(product_id) != 10:
        raise ValueError("Le code produit doit contenir exactement 10 caractères")
    
    # Vérification des caractères alphanumériques
    if not product_id.isalnum():
        raise ValueError("Le code produit ne doit contenir que des caractères alphanumériques")
    
    # Formatage du code avec les tirets
    return f"{product_id[:3]}-{product_id[3:6]}-{product_id[6:]}"


# Exemple d'utilisation
if __name__ == "__main__":
    # Test avec des cas valides
    test_cases = [
        "ABC123DEF4",  # Premier exemple
        "XYZ987GHIJ",  # Deuxième exemple
        "1234567890",  # Chiffres uniquement
        "ABCDEFGHIJ",  # Lettres uniquement
    ]
    
    for code in test_cases:
        try:
            formatted = format_product_code(code)
            print(f"Code original: {code}")
            print(f"Code formaté: {formatted}\n")
        except ValueError as e:
            print(f"Erreur pour {code}: {str(e)}\n")
    
    # Test avec des cas invalides
    invalid_cases = [
        "SHORT",       # Exemple d'erreur donné
        "ABC123",      # Trop court
        "ABC123456789", # Trop long
        "ABC-123DEF",  # Contient un tiret
        "ABC 123DEF",  # Contient un espace
    ]
    
    for code in invalid_cases:
        try:
            format_product_code(code)
        except ValueError as e:
            print(f"Erreur attendue pour {code}: {str(e)}") 