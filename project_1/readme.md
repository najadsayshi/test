

# 🔒 Password Generator Project

## 🌟 Overview
This project is a simple HTML and JavaScript-based password generator featuring a "👀 Show Password" option. It enables users to generate a 🔑 secure password and optionally view it in plain text for ease of use.

## 🎯 Features
1. **🔐 Generate Password**:
   - A 🔘 button that creates a 🎲 random secure password consisting of 🔠 uppercase, 🔡 lowercase letters, 🔢 numbers, and 💥 special characters.

2. **👁️ Show Password**:
   - A ☑️ checkbox to toggle the visibility of the password field, allowing users to see their generated or entered password.

3. **📨 Form Submission**:
   - A 📄 form containing username and password fields.
   - A simulated form submission that displays a ⚠️ confirmation alert.

## 🗂️ File Structure
```
📄 index.html
```

## 🛠️ Code Details
### 🧩 HTML Structure
- A simple 📄 form with the following components:
  - **👤 Username Field** (`type="text"`): Input for the username.
  - **🔒 Password Field** (`type="password"`): Input for the password, initially hidden.
  - **🎲 Generate Password Button**: Generates a secure password.
  - **👁️ Show Password Checkbox**: Toggles password visibility.
  - **📤 Submit Button**: Simulates form submission.

### 💻 JavaScript Functions
1. **🔐 Generate Password**:
   - Generates an 8-character password using a predefined set of characters.
   - Populates the password input field with the generated password.

   ```javascript
   function Generate() {
       const length = 8;
       const charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()";
       let password = "";
       for (let i = 0; i < length; i++) {
           const randomIndex = Math.floor(Math.random() * charset.length);
           password += charset[randomIndex];
       }
       document.getElementById("password").value = password;
   }
   ```

2. **👁️ Show Password**:
   - Toggles the password field between hidden (`type="password"`) and visible (`type="text"`).

   ```javascript
   function togglePasswordVisibility() {
       const passwordField = document.getElementById("password");
       const showPasswordCheckbox = document.getElementById("showPassword");
       if (showPasswordCheckbox.checked) {
           passwordField.type = "text";
       } else {
           passwordField.type = "password";
       }
   }
   ```

3. **📨 Form Submission**:
   - Displays an ⚠️ alert upon form submission.

   ```javascript
   function ok(event) {
       alert("📨 Form submitted!");
       event.preventDefault();
   }
   ```

## 🧑‍💻 How to Use
1. Open the `index.html` file in a 🌐 web browser.
2. Enter a 👤 username in the username field.
3. Click the **🔐 Generate Password** button to generate a secure password.
4. Check the **👁️ Show Password** box to view the password in plain text.
5. Click **📤 Submit** to simulate form submission and view the ⚠️ confirmation alert.

## 🚀 Future Enhancements
- ✏️ Add an option for users to customize the password length.
- 🛠️ Allow users to select character types (e.g., exclude special characters or numbers).
- ✅ Include validation for the username field to ensure input meets specified criteria.

## 🙌 Credits
- **🛠️ Developed by**: Najad
- **💡 Inspired by**: Common password generation tools and best practices.

---

Feel free to customize and expand this project to suit your needs! 🛠️

