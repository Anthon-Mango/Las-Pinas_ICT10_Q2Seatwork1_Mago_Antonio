from pyscript import document

def candidate_checker(e):
    club_members = ["max calata, nathan bernaldez, sophie gamban"]:
    f_name = document.getElementById("max, nathan, sophie").value
    l_name = document.getElementById("calata, bernaldez, gamban").value
    canidate = f_name + '' + l_name

    member_checker = canidate.lower() in club_members
    messages = (f'Sorry {canidate}, your name is not on the list!'
                f'Congratulations {canidate}! your name is in the list!')

document.getElementById('result').InnerHTML = messages[member_checker]
