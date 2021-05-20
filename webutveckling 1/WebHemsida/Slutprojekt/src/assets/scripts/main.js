function copyToClipboard(id)
{
    document.getElementById(id).select()
    document.execCommand("copy") // Kopiera inputen
}

function getYear()
{
    date = new Date()
    return date.getFullYear()
}

function updatePassword(id, length, textId)
{
    generatePassword(id, length)
    var l = document.getElementById(length).value
    if (l < 8)
        document.getElementById(id).style = "color: red;"
    else
        document.getElementById(id).style = "color: green; font-weight: bold;"

    document.getElementById(textId).innerHTML = `Password Length: ${l}`;
}

function generatePassword(id, length) {
    var input = document.getElementById(id)

    // Ifall det är ett nummer så ska den använda det som längd ananrs så ka den ta värdet på slidern
    if (!isNaN(length))
        var l = length;
    else    
        var l = document.getElementById(length).value

    var charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#%&/()={}?_-";
    var password = "";

    for (var i = 0, n = charset.length; i < l; ++i) {
        password += charset.charAt(Math.floor(Math.random() * n));
    }

    input.value = password
}
