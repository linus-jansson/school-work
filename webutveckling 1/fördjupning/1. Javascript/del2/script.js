

async function input() {
    let celcius = parseInt(prompt("Hur många grader i celcius ska omvandlas till fahrenheit?"))

    while (!celcius) {
        celcius = parseInt(prompt("Hur många grader i celcius ska omvandlas till fahrenheit?"))
    }

    let fahrenheit = (celcius * 9/5) + 32
    

    return [fahrenheit, celcius]
}


input().then(r => {
    document.getElementById("output").innerHTML = `${r[1]} Celcius är ${r[0]} fahrenheit`;
})


// alert(fahrenheit)