# Hash Tables and Tree Structures – Cyber Programming Homework

**Course:** CYBF 210 – Cyber Programming  
**Date:** April 30, 2026  

---

## Overview

This assignment explores core data structures used in cybersecurity and computing, including hash tables, collision handling, and tree traversal.

---

## Task 1: Hash Function and Collision Handling

**Hash Function:**  
h(key) = key mod 9

### Computed Values

- 18 → 0 → John  
- 27 → 0 → Ada  
- 36 → 0 → Sarah  
- 20 → 2 → Adam  
- 11 → 2 → Abdul  
- 15 → 6 → George  

---

### Separate Chaining (Using Lists)

| Index | Values |
|------|--------|
| 0 | John → Ada → Sarah |
| 2 | Adam → Abdul |
| 6 | George |

---

### Linear Probing (Open Addressing)

| Index | Values |
|------|--------|
| 0 | John |
| 1 | Ada |
| 2 | Sarah |
| 3 | Adam |
| 4 | Abdul |
| 6 | George |

---

## Key Concept

A hash table stores data by converting keys into indexes, allowing fast lookup (O(1) time complexity).

---

## Task 2: Collisions

A collision occurs when multiple keys map to the same index.

**Example:**  
18, 27, 36 → all map to index 0

---

### Collision Handling Methods

**Separate Chaining**
- Uses lists at each index  
- Better when collisions are frequent  

**Linear Probing**
- Finds next open slot  
- Faster when table is mostly empty  

---

## Task 3: Tree Structure
     55
   /    \
  4      12
 /      /  \
85     5    29


### Node Types
- Leaves: 85, 5, 29  
- Internal Nodes: 55, 4, 12  

---

### Postorder Traversal  
(Left → Right → Root)

Result:  
85, 4, 5, 29, 12, 55

---

## Why This Matters in Cybersecurity

### Password Storage
- Systems store hashed passwords, not raw passwords  
- During login, passwords are hashed and compared  
- Collisions can create security risks  

---

### Fast Lookups (Threat Detection)
Cyber systems handle large datasets:
- IP addresses  
- Login attempts  
- File signatures  

Hash tables allow:
- Instant lookups  
- Real-time threat detection  

---

### Malware and File Integrity
- Files are hashed to detect tampering  
- If the hash changes, the file may be compromised  

Used in:
- Malware detection  
- Digital forensics  
- Software verification  

---

### Collision Attacks
Weak hash functions (like MD5) can be exploited:
- Two different files produce the same hash  
- One safe, one malicious  
- The system cannot distinguish them  

---

## Why This Assignment Matters

This assignment demonstrates:

- Efficient data storage techniques  
- Handling conflicts in systems  
- The relationship between performance and security  

---

## Key Takeaway

This work explores a fundamental question in cybersecurity:

How do systems store and retrieve data instantly without failing when conflicts occur?

This concept is essential in building secure and scalable systems.
