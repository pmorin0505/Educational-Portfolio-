# Week 8 – Project 7: Threat Analysis

## Overview
In this project, I performed threat analysis using OSINT techniques to gather information about different hosts. The goal was to identify potential vulnerabilities and understand their impact using CVE data from Shodan and the National Vulnerability Database (NVD).

## Tools Used
- curl
- Shodan InternetDB API
- National Vulnerability Database (NVD)
- Linux terminal

## Process

### 1. Host Selection and IP Lookup
I selected at least five different hosts and obtained their IP addresses for analysis.

## 2. Collecting Vulnerability Data
For each host IP, I ran the following command:

curl https://internetdb.shodan.io/x.x.x.x

This returned JSON data containing open ports, services, and any known vulnerabilities (CVEs).

## 3. Identifying CVEs
From the returned data, I reviewed the "vulns" field and selected at least three CVEs across different hosts.

Example format:
- Host IP: x.x.x.x
- CVEs found: CVE-XXXX-XXXX

## 4. CVE Research (NVD)
For each selected CVE, I researched it using the National Vulnerability Database to understand:

- What the vulnerability is
- What systems it affects
- Severity level (CVSS score if available)
- Potential real-world impact

## Key Findings

### CVE Analysis
Each CVE was evaluated based on its severity and potential risk. Some vulnerabilities included remote code execution, information disclosure, or outdated service exploitation.

## Key Concepts Learned

### OSINT (Open Source Intelligence)
Gathering publicly available data to analyze systems and potential vulnerabilities.

### CVE Analysis
Understanding standardized vulnerability reports and their real-world impact.

### Threat Assessment
Evaluating how exposed systems could be exploited based on known weaknesses.

## Why This Matters in Cybersecurity
Threat analysis is critical for identifying weaknesses before attackers can exploit them. Tools like Shodan help security professionals:

- Discover exposed systems
- Identify outdated or vulnerable services
- Assess real-world attack risk
- Improve defensive security posture

## Reflection
This project showed how publicly available data can be used to assess cybersecurity risk. It reinforced the importance of vulnerability management and understanding how exposed systems can be identified and analyzed using OSINT tools.
