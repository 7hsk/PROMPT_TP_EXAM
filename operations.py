def addition(a: float, b: float) -> float:
    """
    Effectue l'addition de deux nombres.
    
    Args:
        a (float): Premier nombre
        b (float): Deuxième nombre
        
    Returns:
        float: La somme des deux nombres
    """
    return a + b

def soustraction(a: float, b: float) -> float:
    """
    Effectue la soustraction de deux nombres.
    
    Args:
        a (float): Premier nombre
        b (float): Deuxième nombre
        
    Returns:
        float: La différence entre les deux nombres
    """
    return a - b

def multiplication(a: float, b: float) -> float:
    """
    Effectue la multiplication de deux nombres.
    
    Args:
        a (float): Premier nombre
        b (float): Deuxième nombre
        
    Returns:
        float: Le produit des deux nombres
    """
    return a * b

def division(a: float, b: float) -> float:
    """
    Effectue la division de deux nombres.
    
    Args:
        a (float): Premier nombre (dividende)
        b (float): Deuxième nombre (diviseur)
        
    Returns:
        float: Le quotient des deux nombres
        
    Raises:
        ZeroDivisionError: Si le diviseur est égal à zéro
    """
    if b == 0:
        raise ZeroDivisionError("La division par zéro n'est pas possible")
    return a / b

# Exemple d'utilisation
if __name__ == "__main__":
    # Test des fonctions
    num1 = 10
    num2 = 5
    
    print(f"Addition: {num1} + {num2} = {addition(num1, num2)}")
    print(f"Soustraction: {num1} - {num2} = {soustraction(num1, num2)}")
    print(f"Multiplication: {num1} * {num2} = {multiplication(num1, num2)}")
    print(f"Division: {num1} / {num2} = {division(num1, num2)}") 