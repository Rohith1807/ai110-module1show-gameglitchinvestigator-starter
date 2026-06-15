import sys
import os

# Add parent directory to path so we can import logic_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import check_guess, parse_guess

def test_check_guess_too_high():
    """Test that guessing higher than secret gives correct hint"""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_check_guess_too_low():
    """Test that guessing lower than secret gives correct hint"""
    outcome, message = check_guess(30, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_check_guess_correct():
    """Test that correct guess returns Win"""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

# NEW: Edge case tests
def test_parse_guess_negative_number():
    """Test that negative numbers are rejected"""
    ok, value, error = parse_guess("-50", 1, 100)
    assert ok is False
    assert "between" in error

def test_parse_guess_non_numeric():
    """Test that non-numeric strings are rejected"""
    ok, value, error = parse_guess("abc", 1, 100)
    assert ok is False
    assert "not a valid number" in error

def test_parse_guess_above_range():
    """Test that numbers above range are rejected"""
    ok, value, error = parse_guess("500", 1, 100)
    assert ok is False
    assert "between" in error

def test_parse_guess_decimal_in_range():
    """Test that decimals are converted to int if in range"""
    ok, value, error = parse_guess("50.7", 1, 100)
    assert ok is True
    assert value == 50

def test_parse_guess_empty_string():
    """Test that empty string is rejected"""
    ok, value, error = parse_guess("", 1, 100)
    assert ok is False
    assert "Enter" in error

def test_parse_guess_zero():
    """Test that zero is rejected when min is 1"""
    ok, value, error = parse_guess("0", 1, 100)
    assert ok is False
    assert "between" in error