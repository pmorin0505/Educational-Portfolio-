# Week 3: Project 3 – Password Crack-a-thon

## Overview

This project focused on password security and hash cracking using John the Ripper. The goal was to simulate a real-world password breach scenario and understand how attackers attempt to recover weak or reused passwords from leaked datasets.

The dataset was modeled after real-world breaches such as LinkedIn and Yahoo, where hashed passwords were exposed publicly.

---

## Goals

By the end of this assignment, I was able to:

- Use John the Ripper to crack hashed passwords
- Apply different wordlists to improve cracking success
- Use built-in rule sets to mutate and expand guesses
- Apply custom mask-based cracking strategies
- Analyze cracked results using the `.pot` file output

---

## Dataset Overview

- Total hashes: 1000
- Passwords primarily in English
- Strong concentration of short passwords:
  - 1–4 characters: majority of dataset
  - 5–6 characters: moderate frequency
  - 7–8 characters: very rare

This distribution influenced the cracking strategy by prioritizing shorter passwords first.

---

## Methodology

### 1. Initial Wordlist Attack

The first step was using a basic wordlist provided in the lab environment.

Example command:
john --wordlist=lower.lst cp_leak.txt


This helped identify low-complexity passwords quickly.

---

### 2. Expanded Wordlist Strategy

To improve results, a larger external wordlist was used to increase coverage of common passwords.

Example approach:
- Using rockyou-style wordlists
- Testing common password databases

This significantly increased the number of cracked hashes.

---

### 3. Rule-Based Cracking

Built-in John rules were applied to mutate existing wordlists.

Example command structure:
john --wordlist=wordlist.txt --rules cp_leak.txt


This allowed variations such as:
- Capitalization changes
- Number appending
- Symbol substitution

---

### 4. Mask-Based Attacks

Mask attacks were used to target predictable password structures, especially short passwords.

Example structure:
john --mask=?l?l?l?l cp_leak.txt


This method was effective for 3–5 character passwords based on dataset analysis.

---

### 5. Verifying Results

Cracked passwords were verified using:
john --show cp_leak.txt


This output confirmed which hashes had been successfully recovered.

---

## Key Concepts Learned

### Password Security
Weak and short passwords are significantly easier to crack using automated tools.

### Brute Force vs Smart Attacks
Targeted strategies (wordlists + rules + masks) are more efficient than pure brute force.

### Hash Cracking
Tools like John the Ripper simulate real-world attacker behavior against leaked datasets.

### Security Implications
Short or predictable passwords are highly vulnerable in real breach scenarios.

---

## Why This Matters in Cybersecurity

This assignment demonstrates real-world risks of weak password policies.

Key takeaways:

- Most compromised passwords are short and predictable
- Attackers rely on automation and wordlists
- Security is strengthened by enforcing complexity and length requirements
- Hashing alone is not enough if passwords are weak

---

## Reflection

This project showed how attackers can efficiently recover large numbers of passwords when proper security policies are not enforced.

It reinforced the importance of:
- Strong password creation rules
- Account protection strategies
- Understanding attacker methodologies

It also highlighted how small improvements in password complexity can significantly increase security.
