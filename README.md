# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Describe the game's purpose.
   This project involved debugging a deliberately broken number guessing game built with Streamlit. The game had multiple critical bugs that made it unplayable - from inverted hints to state management issues. Through systematic debugging with AI assistance, I identified 7 distinct bugs, fixed the critical ones, refactored core logic into a separate module, and implemented comprehensive testing.

- Detail which bugs you found.
   1. **Inverted Hints** - When guess > secret, game said "Go HIGHER!" instead of "Go LOWER!"
   2. **Type-Switching Secret** - Secret alternated between int and string on even attempts, breaking comparisons
   3. **Incomplete New Game Reset** - Clicking "New Game" only reset attempts and secret, leaving history/score/status broken
   4. **No Range Validation** - Game accepted -50, 0, 200 despite claiming range was 1-100
   5. **Difficulty Range Ignored** - All difficulties used 1-100 range despite displaying different ranges
   6. **Hard Mode Easier Than Normal** - Hard used 1-50 (easier) vs Normal's 1-100
   7. **New Game Attempts Bug** - Reset to 0 instead of 1, causing off-by-one errors

- Explain what fixes you applied.
   - Fixed inverted hints by swapping message logic in `check_guess()`
   - Removed type conversion bug that converted secret to string on even attempts
   - Fixed incomplete new game reset by resetting all 5 session state variables (attempts, secret, score, history, status)
   - Fixed attempts starting at 0 instead of 1 when new game starts
   - Refactored all game logic functions (`check_guess()`, `parse_guess()`, `get_range_for_difficulty()`, `update_score()`) into `logic_utils.py` for better separation of concerns and testability
   - Added range validation to `parse_guess()` to reject out-of-bounds guesses
   - Implemented comprehensive edge case testing with 9 pytest tests

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

**Game Start:**
1. Player starts game on Normal difficulty (range 1-100)
2. Secret number is 42 (visible in Debug Info)
3. Player has 8 attempts

**Gameplay:**
1. Player guesses **75** → Game shows "📉 Go LOWER!" (correct - 75 > 42)
2. Player guesses **30** → Game shows "📈 Go HIGHER!" (correct - 30 < 42)
3. Player guesses **50** → Game shows "📉 Go LOWER!" (correct - 50 > 42)
4. Player guesses **40** → Game shows "📈 Go HIGHER!" (correct - 40 < 42)
5. Player guesses **45** → Game shows "📉 Go LOWER!" (correct - 45 > 42)
6. Player guesses **42** → Game shows "🎉 Correct!" with balloons animation

**Score Tracking:**
- Score updates after each guess based on outcome
- Final score calculated based on number of attempts
- Game displays win message with final score

**New Game:**
1. Player clicks "New Game 🔁" button
2. Game successfully resets: new secret generated, attempts reset to 0, history cleared, score reset to 0
3. Player can immediately start a fresh game

**Edge Case Handling:**
- Player enters **-50** → Rejected with "Please guess between 1 and 100."
- Player enters **abc** → Rejected with "That is not a valid number."
- Player enters **150** → Rejected with "Please guess between 1 and 100."

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
collected 9 items                                                                                                                         

tests/test_game_logic.py::test_check_guess_too_high PASSED                                                                          [ 11%]
tests/test_game_logic.py::test_check_guess_too_low PASSED                                                                           [ 22%]
tests/test_game_logic.py::test_check_guess_correct PASSED                                                                           [ 33%]
tests/test_game_logic.py::test_parse_guess_negative_number PASSED                                                                   [ 44%]
tests/test_game_logic.py::test_parse_guess_non_numeric PASSED                                                                       [ 55%]
tests/test_game_logic.py::test_parse_guess_above_range PASSED                                                                       [ 66%]
tests/test_game_logic.py::test_parse_guess_decimal_in_range PASSED                                                                  [ 77%]
tests/test_game_logic.py::test_parse_guess_empty_string PASSED                                                                      [ 88%]
tests/test_game_logic.py::test_parse_guess_zero PASSED                                                                              [100%]

=========================================================== 9 passed in 0.10s ============================================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
