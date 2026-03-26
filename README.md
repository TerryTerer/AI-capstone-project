# AI-capstone-project
This is a project aimed at completing my GenAI project

# PASSWORD ANALYZER WITH COHERE AI
# Project Overview
This project demonstrates the use of Cohere's AI API to analyze the strength of passwords.  
The program allows a user to input any password, sends it to Cohere's Chat model, and receives an AI-generated analysis.  
The analysis includes whether the password is weak or strong, what risks it may have, and suggestions to improve it.

# Technology Used: 
Python, Cohere API  

# Project Goal:
Learning how to integrate Cohere’s generative AI models into a Python project for practical applications.

# System Requirements
- OS: Windows, Linux, Mac  
- Python: 3.10+  
- Packages:
  - cohere (v5.20.7)  
  - python-dotenv (to securely store API keys)  


# Installation & Setup

1.Clone or download the project to your local machine.
2.Install Python packages by running:
   bash
   pip install cohere python-dotenv

3.Get a Cohere API key by signing up at [Cohere](https://cohere.com/). It’s free for trial accounts.
4.Create a .env file in the project folder and add your API key:
   COHERE_API_KEY= "your_api_key_here"
   
5.Run the Python script:

   bash
   python passwdchecker.py

# How It Works

1.The script asks the user to input a password.
2.The password is sent to Cohere’s Chat API with a prompt asking it to evaluate the password strength.
3.Cohere returns a response describing:
   *Whether the password is weak, medium, or strong.
   *Potential vulnerabilities.
   *Suggestions to improve the password.
4. The result is printed on the screen for the user.

Example:
Enter a password (or type 'exit'): 12345

Analysis:
Weak password. Too short and predictable. Consider using a mix of letters, numbers, and symbols.

# API Key

*For simplicity, the API key is stored directly in the code:
python
import cohere
co = cohere.Client("YOUR_API_KEY_HERE")


*This works fine for personal testing and submission.
*Optionally, you can use a .env file for safer storage of your key.

# Minimal Example

python
import cohere

co = cohere.Client("YOUR_API_KEY_HERE")

def analyze_password(password):
    response = co.chat(
        model="xlarge",
        query=f"Analyze this password and provide a strength rating: {password}"
    )
    return response.message

password = input("Enter a password (or type 'exit'): ")
while password.lower() != "exit":
    print("Analysis:\n", analyze_password(password))
    password = input("Enter a password (or type 'exit'): ")


# AI Prompt Journal

*Prompt used:"Analyze this password and provide a strength rating"
*AI’s response: Evaluates length, complexity, and common patterns.
*Learning: Cohere can provide helpful, structured analysis of user input for simple security tools.

# Common Issues & Fixes

1.Missing API key: Ensure .env exists and has COHERE_API_KEY.
2.Invalid model name: Make sure you are using model="command" as older models like generate or command-r are deprecated.
3.Package errors: Upgrade cohere to the latest version (pip install --upgrade cohere).

# References

*[Cohere Docs: Chat API](https://docs.cohere.com/docs/chat)
*[Python-dotenv Docs](https://pypi.org/project/python-dotenv/)

