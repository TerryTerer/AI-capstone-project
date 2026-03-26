import cohere
from cohere import ClientV2

# NEW client for SDK 5.x
co = ClientV2(api_key="d65XFtff3aPa55k7RJLI7x8ayerM5HAgcYtByUh2")

def analyze_password(password):
    try:
        response = co.chat(
            model="command-nightly",
            messages=[
                {"role": "system", "content": "You are a cybersecurity expert."},
                {"role": "user", "content": f"Analyze the strength of this password and give suggestions to make it stronger: {password}"}
            ]
        )

        # Extract assistant response
        return response.message.content[0].text

    except Exception as e:
        return f"Error analyzing password: {e}"

while True:
    password = input("Enter a password (or type 'exit'): ")
    if password.lower() == "exit":
        break

    result = analyze_password(password)
    print("\nAnalysis:\n", result, "\n")