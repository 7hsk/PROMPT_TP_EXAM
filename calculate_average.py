def calculate_average(numbers_list):
    """
    Calcule la moyenne des nombres dans une liste.
    
    Args:
        numbers_list (list): Liste de nombres (peut contenir des entiers ou des flottants)
        
    Returns:
        float: La moyenne des nombres arrondie à deux décimales
        
    Raises:
        ValueError: Si la liste est vide ou contient des valeurs non numériques
    """
    if not numbers_list:
        raise ValueError("La liste ne peut pas être vide")
        
    total = 0
    count = 0
    
    for num in numbers_list:
        try:
            # Convertir en float pour gérer à la fois les entiers et les flottants
            num_float = float(num)
            total += num_float
            count += 1
        except (ValueError, TypeError):
            print(f"Attention: '{num}' n'est pas un nombre valide et sera ignoré")
            continue
    
    if count == 0:
        raise ValueError("Aucun nombre valide trouvé dans la liste")
        
    return round(total / count, 2)

# Exemple d'utilisation
my_nums = [1, 2, 'three', 4, 5.5]
try:
    avg = calculate_average(my_nums)
    print(f"Moyenne: {avg}")
except ValueError as e:
    print(f"Erreur: {e}")