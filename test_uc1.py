import pytest
from user import is_valid_First_name  # Import the function from employee.py

def test_valid_first_name():
    assert is_valid_First_name("Shaurya") is True  # First name starting with uppercase followed by lowercase letters

def test_invalid_first_name():
    assert is_valid_First_name("shaurya") is False  # First name starting with lowercase letter
    assert is_valid_First_name("SHAURYA") is False  # First name starting with uppercase but no lowercase letters
    assert is_valid_First_name("Sh") is False  # First name with fewer than 3 characters
    assert is_valid_First_name("S") is False  # Single character name
    assert is_valid_First_name("1234") is False  # First name starting with digits
    assert is_valid_First_name("!@#") is False  # First name with special characters
    assert is_valid_First_name("Shau@") is False  # First name with special characters at the end

def test_edge_case_names():
    assert is_valid_First_name("S") is False  # Single character name should fail
    assert is_valid_First_name("Sha") is True  # Valid 3-letter name


# Run the test cases
if __name__ == "__main__":
    pytest.main()
