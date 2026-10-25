
from pyscript import document

def candidate_checker(e):
    club_members = [
        "max calata",
        "nathan bernaldez",
        "sophie gamban"
    ]

    f_name = document.getElementById("first_name").value.strip()
    l_name = document.getElementById("last_name").value.strip()

    candidate = f"{f_name} {l_name}".strip()

    if candidate.lower() in club_members:
        message = f"Congratulations, {candidate}! Your name is on the list!"
    else:
        message = f"Sorry, {candidate}. Your name is not on the list!"

    document.getElementById("result").textContent = message
