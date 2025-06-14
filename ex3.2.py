#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Module de tri à bulles optimisé avec métadonnées de performance.

Ce module implémente un algorithme de tri à bulles amélioré qui fournit
des informations détaillées sur les performances du tri (nombre de
comparaisons, échanges et temps d'exécution).
"""

from typing import List, TypeVar, Optional, Tuple
from dataclasses import dataclass
import logging
import time
from datetime import datetime

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Type générique pour le tri
T = TypeVar('T', int, float)

@dataclass
class SortResult:
    """
    Résultat du tri avec métadonnées de performance.
    
    Attributes:
        sorted_list: Liste triée
        comparisons: Nombre de comparaisons effectuées
        swaps: Nombre d'échanges effectués
        execution_time: Temps d'exécution en secondes
        timestamp: Date et heure du tri
    """
    sorted_list: List[T]
    comparisons: int
    swaps: int
    execution_time: float
    timestamp: datetime = datetime.now()

def validate_input(numbers: List[T]) -> None:
    """
    Valide les données d'entrée pour le tri.
    
    Args:
        numbers: Liste à valider
        
    Raises:
        ValueError: Si la liste est vide ou contient des types incompatibles
    """
    if not numbers:
        raise ValueError("La liste ne peut pas être vide")
    
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("La liste doit contenir uniquement des nombres")

def perform_swap(
    numbers: List[T],
    j: int,
    ascending: bool
) -> Tuple[bool, int]:
    """
    Effectue un échange si nécessaire et retourne le résultat.
    
    Args:
        numbers: Liste en cours de tri
        j: Index de l'élément à comparer
        ascending: True pour tri croissant, False pour décroissant
        
    Returns:
        Tuple[bool, int]: (True si échange effectué, nombre d'échanges)
    """
    should_swap = (
        numbers[j] > numbers[j + 1] if ascending
        else numbers[j] < numbers[j + 1]
    )
    
    if should_swap:
        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return True, 1
    
    return False, 0

def bubble_sort(
    numbers: List[T],
    ascending: bool = True,
    verbose: bool = False
) -> SortResult:
    """
    Implémente le tri à bulles avec des métadonnées sur les performances.
    
    Args:
        numbers: Liste de nombres à trier
        ascending: True pour tri croissant, False pour décroissant
        verbose: Afficher les étapes intermédiaires si True
    
    Returns:
        SortResult: Objet contenant la liste triée et les métadonnées
        
    Raises:
        ValueError: Si la liste est vide ou contient des types incompatibles
        
    Examples:
        >>> bubble_sort([5, 3, 8, 6, 7, 2])
        SortResult(sorted_list=[2, 3, 5, 6, 7, 8], comparisons=15, swaps=8, ...)
        
        >>> bubble_sort([5, 3, 8, 6, 7, 2], ascending=False)
        SortResult(sorted_list=[8, 7, 6, 5, 3, 2], comparisons=15, swaps=8, ...)
    """
    # Validation des entrées
    validate_input(numbers)
    
    # Initialisation des compteurs
    comparisons = 0
    swaps = 0
    start_time = time.time()
    
    # Copie de la liste pour ne pas modifier l'original
    sorted_numbers = numbers.copy()
    n = len(sorted_numbers)
    
    # Tri à bulles optimisé
    for i in range(n):
        swapped = False
        
        # La dernière i position est déjà triée
        for j in range(0, n - i - 1):
            comparisons += 1
            
            # Effectuer l'échange si nécessaire
            did_swap, swap_count = perform_swap(sorted_numbers, j, ascending)
            swaps += swap_count
            
            if did_swap:
                swapped = True
                if verbose:
                    logger.info(f"Échange: {sorted_numbers}")
        
        # Si aucun échange n'a été fait, la liste est triée
        if not swapped:
            break
    
    execution_time = time.time() - start_time
    
    return SortResult(
        sorted_list=sorted_numbers,
        comparisons=comparisons,
        swaps=swaps,
        execution_time=execution_time
    )

def format_time(seconds: float) -> str:
    """
    Formate le temps d'exécution de manière lisible.
    
    Args:
        seconds: Temps en secondes
        
    Returns:
        str: Temps formaté
    """
    if seconds < 0.001:
        return f"{seconds * 1_000_000:.2f} µs"
    elif seconds < 1:
        return f"{seconds * 1000:.2f} ms"
    return f"{seconds:.2f} s"

def display_sort_results(result: SortResult) -> None:
    """
    Affiche les résultats du tri de manière formatée.
    
    Args:
        result: Résultat du tri à afficher
    """
    print("\n=== Résultats du tri ===")
    print(f"Liste triée: {result.sorted_list}")
    print(f"Nombre de comparaisons: {result.comparisons}")
    print(f"Nombre d'échanges: {result.swaps}")
    print(f"Temps d'exécution: {format_time(result.execution_time)}")
    print(f"Date et heure: {result.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

def run_sort_example(
    numbers: List[T],
    ascending: bool = True,
    verbose: bool = False
) -> None:
    """
    Exécute un exemple de tri avec gestion des erreurs.
    
    Args:
        numbers: Liste à trier
        ascending: True pour tri croissant, False pour décroissant
        verbose: Afficher les étapes intermédiaires si True
    """
    print(f"\nListe originale: {numbers}")
    print(f"Ordre: {'croissant' if ascending else 'décroissant'}")
    
    try:
        result = bubble_sort(numbers, ascending, verbose)
        display_sort_results(result)
    except ValueError as e:
        logger.error(f"Erreur: {e}")

def main() -> None:
    """Fonction principale avec exemples d'utilisation."""
    # Exemple 1: Tri croissant avec verbose
    numbers = [5, 3, 8, 6, 7, 2]
    run_sort_example(numbers, ascending=True, verbose=True)
    
    # Exemple 2: Tri décroissant
    run_sort_example(numbers, ascending=False)
    
    # Exemple 3: Cas d'erreur - liste vide
    run_sort_example([], ascending=True)
    
    # Exemple 4: Cas d'erreur - types mélangés
    run_sort_example([1, "2", 3], ascending=True)

if __name__ == "__main__":
    main()