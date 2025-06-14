def calculate(a: int, b: int, op: str) -> float:
    """
    Effectue une opération mathématique entre deux nombres entiers.
    
    Args:
        a (int): Premier nombre entier
        b (int): Deuxième nombre entier
        op (str): Opérateur mathématique ('+', '-', '*', '/')
        
    Returns:
        float: Résultat de l'opération. Pour la division, le résultat est arrondi à 2 décimales.
        
    Raises:
        ValueError: Si l'opérateur n'est pas valide
        ZeroDivisionError: Si une division par zéro est tentée
    """
    # Vérification de l'opérateur valide
    if op not in ['+', '-', '*', '/']:
        raise ValueError(f"Opérateur invalide: {op}. Utilisez '+', '-', '*' ou '/'")
    
    # Vérification de la division par zéro
    if op == '/' and b == 0:
        raise ZeroDivisionError("Division par zéro impossible")
    
    # Exécution de l'opération appropriée
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:  # op == '/'
        # Arrondir le résultat de la division à 2 décimales
        return round(a / b, 2)

# Exemple d'utilisation
if __name__ == "__main__":
    # Test avec différentes opérations
    test_cases = [
        (10, 5, '+'),  # Addition
        (10, 5, '-'),  # Soustraction
        (10, 5, '*'),  # Multiplication
        (10, 5, '/'),  # Division
        (10, 0, '/'),  # Division par zéro (générera une erreur)
        (10, 5, '%'),  # Opérateur invalide (générera une erreur)
    ]
    
    for a, b, op in test_cases:
        try:
            result = calculate(a, b, op)
            print(f"{a} {op} {b} = {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Erreur pour {a} {op} {b}: {str(e)}") 