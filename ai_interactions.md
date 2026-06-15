# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

**Prompts used to generate edge case tests:**

1. "What are the top 3 edge cases for a function that parses user input into integers for a guessing game?"
2. "Write pytest tests for: negative numbers, non-numeric strings, numbers outside range, decimals, and empty input"

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
| --------- | ----------- | ----------------- | ------------ | -------------- |
| Negative number input | "Test parse_guess with -50" | `test_parse_guess_negative_number()` checks rejection | ✅ Yes | Negative numbers are mathematically valid but logically invalid for a guessing game with range 1-100 |
| Non-numeric string | "Test parse_guess with 'abc'" | `test_parse_guess_non_numeric()` checks ValueError handling | ✅ Yes | Users might type words instead of numbers - need graceful error message |
| Number above range | "Test parse_guess with 500" | `test_parse_guess_above_range()` checks range validation | ✅ Yes | Without bounds checking, users could guess outside game range making hints meaningless |
| Decimal input | "Test parse_guess with 50.7" | `test_parse_guess_decimal_in_range()` checks int conversion | ✅ Yes | Users might enter 50.5 thinking it's valid - we convert to 50 which is reasonable behavior |
| Zero input | "Test parse_guess with 0" | `test_parse_guess_zero()` checks boundary case | ✅ Yes | Zero is valid integer but outside our 1-100 range - important boundary test |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
