<h1>🔐 Secure Password Manager –  App with Encryption</h1>

 ### [YouTube Demonstration](https://youtube.com/@KeenenX)

<h2>Description</h2>

This is a simple and secure password manager built with Python's tkinter for the GUI and cryptography.Fernet for symmetric encryption. It allows you to save and search passwords locally, ensuring they are stored in an encrypted JSON file (vault.json) using a secret key (secret.key).
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python 3.13.3</b> 
- <b>Tkinter</b>

<h2>Environments Used </h2>

- <b>Windows 11</b>

<h2>Program walk-through:</h2>
<!-- Centered Header -->
<div align="center">
  <h1>📦 1. Setup Section – Key and Data Initialization</h1>
  <img src="https://i.imgur.com/p5og6LI.png" height="80%" width="80%" alt="Password generator Steps"/>
  <br/><br/><br/>

  <!-- Subsection 1 -->
  <b>Load or Create Encryption Key:</b><br/>
  <img src="https://i.imgur.com/mdmbixK.png" height="80%" width="80%" alt="Password generator Steps"/><br/>
   "We define file names for the encryption key and the data vault that stores the credentials."
  <br/><br/>

  <!-- Subsection 2 -->
  <b>Load Encrypted Data or Start Fresh:</b><br/>
  <img src="https://i.imgur.com/iQ1sTmO.png" height="80%" width="80%" alt="Password generator Steps"/><br/>
   "If a key already exists, we load it. Otherwise, we generate a new Fernet encryption key and save it to secret.key. This key is then used to create a Fernet object for encryption and decryption."
  <br/><br/>

  <img src="https://i.imgur.com/MHNmr0U.png" height="80%" width="80%" alt="Password generator Steps"/><br/>
   "We check if the data vault (vault.json) exists. If it does, we load the encrypted data; otherwise, we start with an empty dictionary."
  <br/><br/>

  <hr width="80%"/>

  <!-- Step 2 -->
  <h2>💾 2. Save Password Function</h2>
  <img src="https://i.imgur.com/mfz42Qb.png" height="80%" width="80%" alt="Password generator Steps"/><br/>
Retrieves values from the GUI input fields. Validates that site and password aren't empty. Encrypts the password using the fernet object. Saves the email and encrypted password in a dictionary. Dumps this data to the vault.json file. Clears the input fields and shows a success message.
  <br/><br/>
  
  <hr width="80%"/>

  <!-- Step 3 -->
  <h2>🔍 3. Search Password Function</h2>
  <img src="https://i.imgur.com/wmHuCac.png" height="80%" width="80%" alt="Password generator Steps"/><br/>
  Takes the site input from the GUI. Checks if the site is in the saved encrypted data. 
  
  If found: [Decrypts the stored password, Displays both email and password in a popup.]
  
  If not found: [Shows an error message.]
  <br/><br/>

  <hr width="80%"/>

  <!-- Step 4 -->
  <h2>🖼️ 4. GUI – Layout and Components</h2>
  <img src="https://i.imgur.com/oI5B4j7.png" height="80%" width="80%" alt="Password generator Steps"/><br/>
  Builds a clean GUI using Tkinter. 
  
  Form includes three input fields: Site, Email, and Password. 
  
  Two buttons: Save and Search trigger the respective functions. A note at the bottom reminds users that the data is encrypted.
  <br/><br/>


<br />
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
