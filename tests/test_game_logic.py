import sys
import os

# Add parent directory to path so we can import logic_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import check_guess

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
