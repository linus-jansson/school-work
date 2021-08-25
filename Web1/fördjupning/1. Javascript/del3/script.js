let alder = parseInt(prompt("Hur gammal är du i år?"));
let kanLasa
if (alder > 6)
    { kanLasa = confirm("Kan du läsa? Ja eller Nej"); }

let resultat;


if (alder > 6 && alder < 18 && kanLasa == false)
{
    resultat = "Du ska gå i skolan";    
}
else if (alder > 18 && kanLasa == false)
{
    resultat = "Du borde gå en kurs";
}
else if (alder > 6 && alder < 18 && kanLasa == true)
{
    resultat = "Du kan övergå till högre studier";
}
else if (alder <= 6)
{
    resultat = "Du ska gå på dagis"
}
else
{
    resultat = "Något fel hände som jag inte har tänkt på i programmet";
}

document.getElementById("output").innerHTML = resultat;