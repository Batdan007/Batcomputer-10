import os
from termcolor import cprint

    
if (os.environ.get("TOGETHER_API_KEY") is None
    or os.environ.get("TOGETHER_API_KEY") == "f71cba20dd0227f6172b60df252da2358850afead52a458bca1f3760c11910e9"
):
    cprint(
        "\nYou can get your Together API key from https://together.xyz/account/api-keys"
    )
    TOGETHER_API_KEY = input("Enter your Together API key: ")
    # Write the API key to the .env file if TOGETHER_API_KEY is not set write it inside the "string"
    with open(".env", "a") as f:
        f.write(f'\n\nTOGETHER_API_KEY="f71cba20dd0227f6172b60df252da2358850afead52a458bca1f3760c11910e9"')
