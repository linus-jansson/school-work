let randInt = Math.floor(Math.random() * 100) + 1;

let gissning = parseInt(prompt("gissa på ett nummer 1-100"))

while (gissning != randInt)
{

    if (gissning > randInt)
        alert("Du gissade för högt");
    else if (gissning < randInt)
        alert("Du gissade för lågt");
    else 
        break;
    
    gissning = parseInt(prompt("gissa på ett nummer 1-100"))

}

document.write("<p>Du gissade rätt!</p>")
