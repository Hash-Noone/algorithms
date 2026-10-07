# 01. Valid Palindrome

**Topic:** Two Pointers  |  **Pattern:** Opposite-direction pointers

## Question

A phrase is a palindrome if, after converting all uppercase letters to lowercase and removing every character that is not a letter or digit, it reads the same forwards and backwards.

Given a string `s`, return `True` if it is a palindrome, otherwise `False`.

## Examples

**Example 1**

```
Input:  s = 'A man, a plan, a canal: Panama'
```

Expected output: `True`

Explanation: "amanaplanacanalpanama" reads the same in both directions.

**Example 2**

```
Input:  s = 'race a car'
```

Expected output: `False`

Explanation: "raceacar" is not the same reversed.

**Example 3**

```
Input:  s = ' '
```

Expected output: `True`

Explanation: After removing non-alphanumeric characters the string is empty, and an empty string is a palindrome.

## Constraints

- `0 <= len(s) <= 200000`
- `s` contains printable ASCII characters

## Your task

Implement `valid_palindrome` in [`solution.py`](solution.py).

```python
def valid_palindrome(s: str) -> bool:
```

## Hint

Put one pointer at each end. Skip anything that is not alphanumeric, compare the two characters (ignoring case), then move both inward.

## Check your work

```bash
python test.py          # tests your solution.py
(try it yourself first!)
```
