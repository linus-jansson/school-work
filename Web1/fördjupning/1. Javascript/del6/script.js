function converter() {

    async function input() {
        let celcius = parseInt(prompt("Hur många grader i celcius ska omvandlas till fahrenheit?"))
    
        let fahrenheit = (celcius * 9/5) + 32
        
        return [fahrenheit, celcius]
    }
    
    
    input().then(r => {
        if (r)
            document.getElementById("output").innerHTML = `${r[1]} Celcius är ${r[0]} fahrenheit`;
    })
    
}

function adition() {
    let numOne = parseInt(prompt("Skriv in ett nummer"))
    let numTwo = parseInt(prompt("Skriv in ett till nummer"))

    document.getElementById("output").innerHTML = `${numOne} + ${numTwo} = ${numOne + numTwo}`;
}

function subtract() {
    let numOne = parseInt(prompt("Skriv in ett nummer"))
    let numTwo = parseInt(prompt("Skriv in ett till nummer"))

    document.getElementById("output").innerHTML = `${numOne} - ${numTwo} = ${numOne - numTwo}`;
}


function secret() {
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

    document.getElementById("output").innerHTML = "<p>Du gissade rätt!</p>"

}

function exit() {
    document.getElementById("meny").innerHTML = "<h1>Tack!</h1>"
}