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
|Click "New Game" button |Should reset history, score, status to fresh state |History persists, score stays, game doesn't fully reset |none- "Game over. Start a new game to try again" same line stays without any changes. |
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

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I asked: "Why doesn't the new game button work?"
The AI initially suggested it was a Streamlit caching issue and recommended using `@st.cache_data`. This was incorrect - the real issue is that the new_game logic only resets `attempts` and `secret`, but leaves `history`, `score`, and `status` in their old state. I verified this by checking the Developer Debug Info after clicking "New Game" - the history list still showed my previous guesses.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
