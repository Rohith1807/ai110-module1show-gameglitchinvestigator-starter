# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran the game, it was completely unplayable. 
  - The hints contradicted themselves
  - the game state never reset properly
  - the logic seemed to change randomly between attempts.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
Concrete bugs noticed at the start:
  - The hints were backwards: when I guessed 25 and the secret was 27, it told me "Go LOWER!"
  - Clicking "New Game" didn't actually start a fresh game - my history and score persisted
  - The game accepted -24 and 2000000 as valid guesses despite claiming the range was 1-100

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess: 25, Secret: 27 |Should show "📈 Go HIGHER!" |Shows "📉 Go LOWER!" |none |
| Click "New Game" button | Should reset history, score, status, attempts to fresh state | History persists, score stays at old value, status not reset, attempts starts at 0 instead of 1 | "New game started." message appears but state is incompletely reset |
|Guess: -34 |Should reject with "out of range" error |Accepts and gives misleading hint  |none |
|Guess on attempt #2 (even)|Should compare integers normally|Compares integer guess to string secret, breaks logic|none|
|Select "Hard" difficulty|Should use range 1-50|Uses range 1-100 (same as Normal)|Sidebar shows "Range: 1 to 50" but secret is 1-100|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude AI

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked: "Why do the hints show the opposite of what they should?"
The AI correctly identified that the logic in `check_guess()` had the "Too High" and "Too Low" branches swapped. When `guess > secret`, it returns "Too High" status but displays "Go HIGHER!" message. I verified this by tracing through the code and seeing the exact inversion on lines 41-44.

**Another correct AI suggestion:**
I asked: "When I click New Game, my history and score don't reset. What am I missing?"

The AI correctly pointed out that the new_game button logic on line 142 only resets `attempts` and `secret`, but leaves `history`, `score`, and `status` in their old values. It suggested resetting all five session state variables: attempts (to 1, not 0), secret, score (to 0), history (to empty list), and status (to "playing").

I verified this by:
1. Adding all five resets to the new_game block
2. Playing a game with several guesses
3. Clicking "New Game" and checking Debug Info - all values now properly reset
4. Starting fresh games multiple times - each started clean

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I asked: "Why doesn't the new game button work?"
The AI initially suggested it was a Streamlit caching issue and recommended using `@st.cache_data`. This was incorrect - the real issue is that the new_game logic only resets `attempts` and `secret`, but leaves `history`, `score`, and `status` in their old state. I verified this by checking the Developer Debug Info after clicking "New Game" - the history list still showed my previous guesses.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  A bug was really fixed when: 1) the pytest test passed, 2) the manual game test worked as expected, and 3) no new bugs appeared.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  **Manual test I ran:**
  After fixing the inverted hints bug, I ran the game with the secret at 42. I guessed 60 - it correctly showed "📉 Go LOWER!". Then I guessed 20 - it correctly showed "📈 Go HIGHER!". Finally I guessed 42 and won. This confirmed the logic now matched expected behavior.

  **Automated test:**
  I wrote `test_check_guess_too_high()` which calls `check_guess(60, 50)` and asserts the outcome is "Too High" and the message contains "LOWER". When this passed, it proved the hint logic was fixed at the function level, independent of the Streamlit UI.

- Did AI help you design or understand any tests? How?
  AI helped me design the test by suggesting edge cases and the correct assertion structure. It also explained why testing the function in isolation (in logic_utils.py) was better than testing through the Streamlit UI - easier to debug and faster to run.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - I'd explain it to a friend like this: "Imagine you're writing on a whiteboard, and every time someone clicks a button or types something, someone walks in and erases the entire whiteboard and makes you start writing from scratch. That's Streamlit - every interaction triggers a complete rerun of your entire Python script from top to bottom. If you just use regular variables like `secret = 42`, they get reset to 42 every single time, so your game would pick a new secret number with every guess! That's why we need `st.session_state.secret = 42` - it's like writing in permanent marker on a separate piece of paper that doesn't get erased. Streamlit remembers what's in session_state between reruns, so your secret number, score, and history survive button clicks."

  - The key insight I gained: Streamlit's execution model is fundamentally different from regular Python scripts. In a normal program, variables persist until you explicitly change them. In Streamlit, you have to explicitly mark which data should persist (session_state) versus which can be recalculated each time (regular variables). This bit me hard when debugging the "New Game" button - I had to reset FIVE separate session_state variables (attempts, secret, score, history, status) because each one persisted independently.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - I want to keep the practice of **writing tests immediately after fixing a bug, not later**. In this project, I wrote `test_check_guess_too_high()` right after fixing the inverted hints, and `test_parse_guess_negative_number()` right after adding range validation. This gave me instant confidence the fixes were correct and created a safety net against regressions. It's much better than my old habit of "run the app and see if it looks right" because tests are repeatable, fast, and don't require manual checking every time I change something.

- What is one thing you would do differently next time you work with AI on a coding task?
  - Next time working with AI on coding, I'll **paste the specific code block I'm asking about** instead of just describing symptoms vaguely. When I asked "why does the game break on even attempts?" without context, the AI guessed it was a Streamlit caching issue. When I finally showed it the actual lines with `secret = str(st.session_state.secret)`, it immediately identified the type conversion bug. Context is everything with AI - show don't tell. Also, I'd be more careful about removing old code after refactoring - I had duplicate functions in app.py that overrode my imports, which wasted debugging time.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - Before this project, I thought AI-generated code was either "correct" or "wrong" - like a binary pass/fail. Now I understand it's more like getting a first draft from a smart but inexperienced teammate. The code might be 90% correct with subtle bugs, or completely right but not the best approach, or confidently wrong if I didn't give enough context. My job as the developer is to read every line critically, understand what it's actually doing, test it thoroughly, and verify it solves my specific problem. AI is a powerful accelerator, but I'm still the one responsible for code quality and correctness.
