import pytest
from product_code import format_product_code

def test_valid_product_codes():
    # Test avec des codes valides
    assert format_product_code("ABC1234567") == "ABC-1234-567"
    assert format_product_code("1234567890") == "123-4567-890"
    assert format_product_code("ABCDEFGHIJ") == "ABC-DEFG-HIJ"

def test_invalid_length():
    # Test avec des codes de longueur invalide
    with pytest.raises(ValueError) as exc_info:
        format_product_code("ABC123")
    assert "10 caractères" in str(exc_info.value)
    
    with pytest.raises(ValueError) as exc_info:
        format_product_code("ABC123456789")
    assert "10 caractères" in str(exc_info.value)

def test_invalid_characters():
    # Test avec des caractères non alphanumériques
    with pytest.raises(ValueError) as exc_info:
        format_product_code("ABC-123456")
    assert "alphanumériques" in str(exc_info.value)
    
    with pytest.raises(ValueError) as exc_info:
        format_product_code("ABC 123456")
    assert "alphanumériques" in str(exc_info.value)
    
    with pytest.raises(ValueError) as exc_info:
        format_product_code("ABC@123456")
    assert "alphanumériques" in str(exc_info.value) 