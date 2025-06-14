import pytest
from calculate_average import calculate_average

def test_valid_numbers():
    """Test avec des nombres valides (entiers et flottants)"""
    # Test avec des entiers
    assert calculate_average([1, 2, 3, 4, 5]) == 3.0
    
    # Test avec des flottants
    assert calculate_average([1.5, 2.5, 3.5]) == 2.5
    
    # Test avec un mélange d'entiers et de flottants
    assert calculate_average([1, 2.5, 3, 4.5]) == 2.75

def test_mixed_values():
    """Test avec des valeurs mixtes (nombres et non-nombres)"""
    # Test avec une chaîne de caractères
    result = calculate_average([1, 2, 'three', 4])
    assert result == 2.33  # (1 + 2 + 4) / 3
    
    # Test avec plusieurs types non numériques
    result = calculate_average([1, 'a', 2, 'b', 3])
    assert result == 2.0  # (1 + 2 + 3) / 3

def test_empty_list():
    """Test avec une liste vide"""
    with pytest.raises(ValueError) as exc_info:
        calculate_average([])
    assert "La liste ne peut pas être vide" in str(exc_info.value)

def test_all_invalid_values():
    """Test avec uniquement des valeurs non numériques"""
    with pytest.raises(ValueError) as exc_info:
        calculate_average(['a', 'b', 'c'])
    assert "Aucun nombre valide trouvé" in str(exc_info.value)

def test_single_number():
    """Test avec un seul nombre"""
    assert calculate_average([5]) == 5.0
    assert calculate_average([5.5]) == 5.5

def test_negative_numbers():
    """Test avec des nombres négatifs"""
    assert calculate_average([-1, -2, -3]) == -2.0
    assert calculate_average([-1.5, 2.5, -3.5]) == -0.83

def test_zero_values():
    """Test avec des zéros"""
    assert calculate_average([0, 0, 0]) == 0.0
    assert calculate_average([0, 1, 2]) == 1.0

def test_large_numbers():
    """Test avec des grands nombres"""
    assert calculate_average([1000, 2000, 3000]) == 2000.0
    assert calculate_average([1e6, 2e6, 3e6]) == 2e6

def test_decimal_precision():
    """Test de la précision décimale (arrondi à deux décimales)"""
    result = calculate_average([2.345, 2.345, 2.345])
    assert result == 2.35  # Vérifie l'arrondi à 2 décimales 