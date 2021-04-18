function copyToClipboard(id)
{
    var input = document.getElementById(id)
    input.select()
    document.execCommand("copy") // Kopiera inputen
}

function getYear()
{
    date = new Date()
    return date.getFullYear()
}

function updateHTML(elmId, value) {
    var elem = document.getElementById(elmId);
    if(typeof elem !== 'undefined' && elem !== null) {
      elem.innerHTML = value;
    }
    else
    {
        console.log(`updateHTML -> element: ${elem} doesn't exist`)
    }
}

function getInputVal(elmId) {
    var elem = document.getElementById(elmId)
    if (typeof elem !== 'undefined' && elem !== null) {
        return elem.value
    }
    else
    {
        console.log(`getinputVal() -> element: ${elem} doesn't exist`)
    }
}

function generatePassword(id) {
    var input = document.getElementById(id)

    var length = 16;
    var charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#%&/()={}?_-";
    var password = "";

    for (var i = 0, n = charset.length; i < length; ++i) {
        password += charset.charAt(Math.floor(Math.random() * n));
    }

    input.value = password
}
