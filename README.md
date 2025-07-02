<p align="center">
  <img src="./hstuLogo.png" alt="HSTU-Logo" width="150">
</p>

<h2 align="center"><strong>Hajee Mohammad Danesh Science and Technology University</strong></h2>
<h3 align="center">Dinajpur-5200</h3>

---
<h1 align="center"><strong><img src="./image1.png" width="32"> SR-121</strong></h1>
<p align="center">A Symmetric Letter-Digit Cryptographic Algorithm</p>

---

### Course Information
- **Course Title:** Mathematical Analysis for Computer Science  
- **Course Code:** CSE 361  

---

### Submitted By

- **Name:** Sourav Roy  
- **Student ID:** 2102008  
- **Level:** 3  
- **Semester:** II  
- **Department:** Computer Science and Engineering

  ---

### 🧑‍🏫 Submitted To

 - **Name:** Pankaj Bhowmik  
 - **Designation:** Lecturer  
 - **Department:** Computer Science and Engineering

---

### 🧠 Algorithm Philosophy:
SR is a custom-designed symmetric cryptographic algorithm developed to encrypt and decrypt messages composed of letters and digits. It is designed for secure handling of variable-length input. 

---

## ✨ Core Functionalities:

- **Symmetric Encryption**  
  Uses the same transformation logic for both encryption and decryption, ensuring perfect reversibility without complex key exchanges.

- **Letter & Digit Support**  
  Fully supports alphanumeric characters, including uppercase/lowercase letters (`A–Z`, `a–z`) and numerical digits (`0–9`).

- **Flexible Input Size**  
  Capable of encrypting and decrypting strings of any length, from single characters to full sentences or codes.

- **Custom Logic**  
  Built on original algorithmic principles designed by the author, ideal for educational, experimental, and lightweight cryptographic applications.

---

---

## Position Table: 
<img src="./table.png">

---

## 🔐 Encryption Process:

The encryption process follows a position-aware and key-based mapping system. Here's a step-by-step breakdown:

### 📥 Steps for Encryption:

1. **Determine position:**  
   Let `xi` be the position (0–35) of the *i-th* character from the plaintext, using the character-to-value table.

2. **Extend key:**  
   Repeat or truncate the key's digits to match the length of the plaintext. Let `Ki` be the digit at position *i* in the extended key.

3. **Compute new position according to key:**  
   Calculate the transformed index using:
   
<br>

  ` Ni = (xi + ⌊(K/2)⌋ } mod 36 `

<br>
    
   where `K` is the key , ⌊(k/2)⌋ will give the floor value of the result after dividing the key by 2.
   
<br>
4. **Now Encrypt using the following formula:**  
   
`Ci= [Ki + {(Ni+121) mod 36}] mod 36`

<br>

where, `Ki` is the position value of the ` i-th `digit of the key. 


5. **Map to encrypted character:**  
   Use the value of `Ci` from  the position table.

---



