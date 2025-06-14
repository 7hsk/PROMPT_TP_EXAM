def math_operations(a: int, b: int, op: str) -> float:
    """
    Effectue une opération mathématique entre deux nombres entiers.
    
    Cette fonction prend deux entiers et un opérateur mathématique en entrée,
    effectue l'opération correspondante et retourne le résultat.
    
    Args:
        a (int): Premier opérande
        b (int): Deuxième opérande
        op (str): Opérateur mathématique ('+', '-', '*', '/')
        
    Returns:
        float: Résultat de l'opération. Les divisions sont arrondies à 2 décimales.
        
    Raises:
        ValueError: Si l'opérateur n'est pas valide
        ZeroDivisionError: Si une division par zéro est tentée
        
    Examples:
        >>> math_operations(10, 5, '+')
        15
        >>> math_operations(10, 3, '/')
        3.33
    """
    # Liste des opérateurs valides
    VALID_OPERATORS = ['+', '-', '*', '/']
    
    # Vérification de la validité de l'opérateur
    if op not in VALID_OPERATORS:
        raise ValueError(
            f"Opérateur '{op}' non valide. "
            f"Utilisez l'un des opérateurs suivants: {', '.join(VALID_OPERATORS)}"
        )
    
    # Vérification de la division par zéro
    if op == '/' and b == 0:
        raise ZeroDivisionError("Division par zéro impossible")
    
    # Dictionnaire des opérations
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: round(x / y, 2)
    }
    
    # Exécution de l'opération
    return operations[op](a, b)


def main():
    """
    Fonction principale pour tester math_operations avec différents cas.
    """
    # Cas de test
    test_cases = [
        (10, 5, '+', "Addition"),
        (10, 5, '-', "Soustraction"),
        (10, 5, '*', "Multiplication"),
        (10, 5, '/', "Division"),
        (10, 0, '/', "Division par zéro"),
        (10, 5, '%', "Opérateur invalide")
    ]
    
    # Exécution des tests
    for a, b, op, description in test_cases:
        try:
            result = math_operations(a, b, op)
            print(f"{description}: {a} {op} {b} = {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"{description}: Erreur - {str(e)}")


if __name__ == "__main__":
    main() 