from pyscript import document

def intrams_checker(e):

    document.getElementById('output').innerHTML = ''
    document.getElementById('image').innerHTML = ''

    body = document.getElementById("pageBody")
    default_color = "rgb(72, 71, 71)"

    # Safely check selected radio buttons
    reg_selected = document.querySelector('input[name="registration"]:checked')
    clear_selected = document.querySelector('input[name="clearance"]:checked')

    if reg_selected is None or clear_selected is None:
        document.getElementById("output").innerHTML = "Please answer all the questions."
        body.style.backgroundColor = default_color
        document.getElementById("teamLogo").src = "logo.png"
        return

    registration = reg_selected.value
    clearance = clear_selected.value

    grade_level = int(document.getElementById('level').value)
    section = document.getElementById('section').value


    if registration != 'registered':

        document.getElementById("output").innerHTML = "Not eligible: student is not registered for Intrams. Ask your PE teacher regarding the online registration."

        body.style.backgroundColor = default_color
        document.getElementById("teamLogo").src = "logo.png"


    elif clearance != 'cleared':

        document.getElementById("output").innerHTML = "Not eligible: medical clearance required. Go to the clinic and secure your clearance."

        body.style.backgroundColor = default_color
        document.getElementById("teamLogo").src = "logo.png"


    elif section == 'emerald':

        document.getElementById("output").innerHTML = 'Congratulations! You are part of the <b style="color:#2ecc71">GREEN HORNETS</b>!'

        document.getElementById("image").innerHTML = "<img src='Green.png' width='200'>"

        document.getElementById("teamLogo").src = "Green.png"

        body.style.backgroundColor = "#2ecc71"


    elif section == 'ruby':

        document.getElementById("output").innerHTML = 'Congratulations! You are part of the <b style="color:#e74c3c">RED BULLDOGS</b>!'

        document.getElementById("image").innerHTML = "<img src='Red.png' width='200'>"

        document.getElementById("teamLogo").src = "Red.png"

        body.style.backgroundColor = "#e74c3c"


    elif section == 'sapphire':

        document.getElementById("output").innerHTML = 'Congratulations! You are part of the <b style="color:#3498db">BLUE BEARS</b>!'

        document.getElementById("image").innerHTML = "<img src='Blue.png' width='200'>"

        document.getElementById("teamLogo").src = "Blue.png"

        body.style.backgroundColor = "#3498db"


    else:

        document.getElementById("output").innerHTML = 'Congratulations! You are part of the <b style="color:#f1c40f">YELLOW TIGERS</b>!'

        document.getElementById("image").innerHTML = "<img src='Yellow.png' width='200'>"

        document.getElementById("teamLogo").src = "Yellow.png"

        body.style.backgroundColor = "#f1c40f"