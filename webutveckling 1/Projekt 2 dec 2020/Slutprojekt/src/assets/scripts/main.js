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