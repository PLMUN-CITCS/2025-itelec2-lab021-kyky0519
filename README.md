# 2025-ITELEC2-LAB021
Week 05 - Working with Functions

Laboratory # 21 - Group Activity # 01 - Problem 03: Factorial Calculator with Input and Calculation Functions

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 21 - Group Activity # 01 - Problem 03: Factorial Calculator with Input and Calculation Functions**

   **Objective:**
   This challenge focuses on building a program that performs a specific mathematical calculation (factorial) while emphasizing function design and basic input handling. You will practice:
   - Creating functions with distinct roles.
   - Implementing a loop for iterative calculations.
   - Handling user input and basic validation (optional extension).
   - Returning values from functions and using them in the main program.

   **Desired Output:**
   ```bash
   Enter a non-negative integer: 6
   The factorial of 6 is: 720
   
   Enter a non-negative integer: 0
   The factorial of 0 is: 1
   ```
   
   **Notable Observations (to be discussed after completing the exercise):**
   - Function Decomposition: The program is divided into two functions: get_non_negative_integer for input handling and calculate_factorial for the factorial calculation. This promotes modularity and code organization.
   - Iterative Calculation: The calculate_factorial function uses a loop to iteratively multiply numbers, which is the core logic of calculating a factorial.
   - Base Case: The factorial function handles the base case of 0! (factorial of 0) by returning 1.

   **Python Best Practices**
   - Meaningful Function and Variable Names: Use descriptive names that clearly indicate the purpose of functions and variables (e.g., get_non_negative_integer, calculate_factorial, n).
   - Docstrings: Include docstrings for each function to explain its purpose, parameters, and return value.
   - Type Hints (Optional but Recommended): Use type hints to specify the expected data types for function parameters and return values.
   - Input Validation (Challenge Extension): Consider adding input validation to the get_non_negative_integer function to handle cases where the user enters invalid input (e.g., negative numbers, non-numeric input). This could involve a loop and a try-except block to repeatedly prompt the user until a valid non-negative integer is entered.
   - Test Thoroughly: Test your program with various inputs, including different non-negative integers (e.g., 0, 5, 10) and potentially invalid inputs (if you implement input validation) to ensure it works correctly in all cases.

   **Challenge Requirements:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `factorial_calculator_functions.py`
      
   2. get_non_negative_integer() Function:
      - Purpose: Obtains a non-negative integer input from the user.
      - No parameters.
      - Prompts the user to enter a non-negative integer.
      - Reads and converts the input to an integer data type.
      - (Optional) Validates the input to ensure it is greater than or equal to 0.
      - Returns the validated non-negative integer.
      
   3. calculate_factorial(n) Function:
      - Purpose: Calculates the factorial of a given non-negative integer.
      - Takes one parameter: n (non-negative integer).
      - Handles the base case: If n is 0, return 1.
      - For n greater than 0, uses a loop (e.g., for loop) to iterate from 1 to n (inclusive) and calculate the factorial by multiplying the numbers in each iteration.
      - Returns the calculated factorial.

   4. Main Program Flow
      - Calls get_non_negative_integer() to get a valid input number.
      - Calls calculate_factorial(), passing the returned number as an argument.
      - Displays the calculated factorial to the user in a descriptive message (e.g., "The factorial of 6 is: 720").

   **Conclusion**
   This challenge helps you practice creating functions with specific purposes and combining them to solve a mathematical problem. It also emphasizes the importance of handling user input and considering potential edge cases (like the factorial of 0). By decomposing the problem into functions and following best practices, you can create more organized, readable, and maintainable code.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 05 - Laboratory # 21"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
