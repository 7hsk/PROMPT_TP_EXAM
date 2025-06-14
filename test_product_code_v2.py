import pytest
from product_code_v2 import format_product_code

def test_valid_product_codes():
    # Test avec des codes valides
    assert format_product_code("ABC123DEF4") == "ABC-123-DEF4"
    assert format_product_code("XYZ987GHIJ") == "XYZ-987-GHIJ"
    assert format_product_code("1234567890") == "123-456-7890"
    assert format_product_code("ABCDEFGHIJ") == "ABC-DEF-GHIJ"

def test_invalid_length():
    # Test avec des codes de longueur invalide
    with pytest.raises(ValueError) as exc_info:
        format_product_code("SHORT")
    assert "10 caractères" in str(exc_info.value)
    
    with pytest.raises(ValueError) as exc_info:
        format_product_code("ABC123")
    assert "10 caractères" in str(exc_info.value)
    
    with pytest.raises(ValueError) as exc_info:
        format_product_code("ABC123456789")
    assert "10 caractères" in str(exc_info.value)

def test_invalid_characters():
    # Test avec des caractères non alphanumériques
    with pytest.raises(ValueError) as exc_info:
        format_product_code("ABC-123DEF")
    assert "alphanumériques" in str(exc_info.value)
    
    with pytest.raises(ValueError) as exc_info:
        format_product_code("ABC 123DEF")
    assert "alphanumériques" in str(exc_info.value)
    
    with pytest.raises(ValueError) as exc_info:
        format_product_code("ABC@123DEF")
    assert "alphanumériques" in str(exc_info.value) 