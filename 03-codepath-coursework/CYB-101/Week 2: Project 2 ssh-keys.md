# Week 2: Project 2 – All About SSH Keys

## Overview

In this project, I learned how to generate and use SSH keys for authentication, encryption, and integrity. SSH keys are commonly used in cybersecurity to securely access systems, protect data, and verify that files have not been altered.

---

## Goals

By the end of this assignment, I was able to:

- Generate SSH key pairs for secure authentication
- Use SSH keys for encryption and decryption with OpenSSL
- Verify integrity of Git commits using SSH signing

---

## Part 1: SSH Key Generation

I generated an RSA SSH key pair using the following command: ssh-keygen -t rsa -b 4096 -C "CYB101 Ubuntu Key"


This created:
- A private key (kept secure locally)
- A public key (used for authentication and sharing)

The keys were stored in the `.ssh` directory and verified using `cat`.

---

## Part 2: Authentication

SSH keys were used to authenticate into a remote environment without needing a password.

Key steps included:
- Copying the SSH key to the VM using `ssh-copy-id`
- Downloading the key using `scp`
- Logging in using `ssh -i` with the private key

This demonstrated how SSH key-based authentication improves security compared to password-based login.

---

## Part 3: Encryption and Decryption

I used OpenSSL with SSH keys to encrypt and decrypt a file.

Commands used:
openssl genrsa -out ~/.ssh/privatekey.pem 2048
openssl rsa -in ~/.ssh/privatekey.pem -out ~/.ssh/publickey.pem -pubout

A sample message file was created:

echo "MY SECRET MESSAGE" > secret.txt

Encryption:
openssl pkeyutl -encrypt -pubin -inkey ~/.ssh/publickey.pem -in secret.txt -out secret.txt.encrypted


Decryption:
openssl pkeyutl -decrypt -inkey ~/.ssh/privatekey.pem -in secret.txt.encrypted -out secret.txt.decrypted


This showed how public key encryption protects data and ensures only the private key holder can decrypt it.

---

## Part 4: Integrity with Git Signing

I configured Git to use SSH signing to verify commit integrity.

Key steps included:

- Initializing a Git repository
- Configuring user information
- Enabling commit signing:

git config --global commit.gpgsign true
git config --global gpg.format ssh


- Adding SSH key to ssh-agent
- Registering signing key in Git
- Making a signed commit:
git commit --allow-empty --message="SSH signing test"


Verification:
git show --show-signature
