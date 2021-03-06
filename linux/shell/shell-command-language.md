
# Shell Command Language

  * This is the 2nd chapter of [The Open Group Base Specifications Issue 6, 2004 edition](https://pubs.opengroup.org/onlinepubs/009695399/utilities/xcu_chap02.html)
  * It contains the definition of the Shell Command Language

----

## 1. Shell Introduction

---

## 2. Quoting

---

## 3. Token Recognition

---

## 4. Reserved Words


---

## 5. Parameters and Variables

### 5.1. Positional paramters

### 5.2. Special parameters

### 5.3. Shell variables


---

## 6. Word Expansions

  * Not all expansions are performed on every word
    * Expand in a single word to a single field: Tilde expansion, parameter expansion, command substitution, arithmetic expansion and quote removal 
	* Create multiple fields from a single world: field splitting, pathname expansion
	* Exception: expansion of special parameter `@` within double-quotes
  * The order of word expansion:
    1. Tilde expansion, parameter expansion, command substitution, arithmetic expansion
	2. Field splitting: performed on the portions of the fields generated by step 1, unless `IFS` is null
	3. Pathname expansion: unless `set -f` is in effect
	4. Quote removal: always performed last
  * The expansions occurs in the same shell environment as that in which the command is executed
  * If the complete expansion appropriate for a word results in an empty field, the empty field shall be deleted from the list of the fields that form the completely expanded command, unless the orignal word contained single-quote or double quote characters
  * The `$` character is used to introduce parameter expansion, command substitution, or arithmetic evaluation.
  * If an unquoted `$` is followed by a character that is either not numeric, the name of one of the special parameters, a valid first character of a variable name, a left curly brace `{` or a left parenthesis, the result is unspecified.

---

### 6.1. Tilde Expansion

---

### 6.2. Parameter Expansion

---

### 6.3. Command Substitution

---

### 6.4. Arithmetic Expansion


---

### 6.5. Field Splitting


### 6.6. Pathname Expansion


### 6.7. Quote Removal

---

## 7. Redirection


---

## 10. Exit Status and Errors


---

## 9. Shell Commands


---

## 10. Shell Grammar


---

## 11. Signals and Error Handling

---

## 12. Shell Execution Environment


---

## 13. Pattern Matching Notation


---

## 14. Speical Built-In Utilities


---

## References

  * [The Open Group Base Specifications Issue 6, 2004 edition](https://pubs.opengroup.org/onlinepubs/009695399/utilities/xcu_chap02.html)
  * [The Open Group Base Specifications Issue 7, 2018 edition](https://pubs.opengroup.org/onlinepubs/9699919799/)
