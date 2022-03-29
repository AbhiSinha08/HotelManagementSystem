const page = document.getElementById("export_btns")
const btns = page.querySelectorAll("button")

function downloadURI(uri) 
{
    var link = document.createElement("a");
    link.setAttribute('download', '');
    link.href = uri;
    document.body.appendChild(link);
    link.click();
    link.remove();
}

async function getCSV(id) {
    response = await fetch('/export/' + id);
    response.text().then((filename) => {
        downloadURI(filename);
    })
}

for (let btn of btns) {
    const id = btn.id;
    btn.addEventListener('click', () => {
        getCSV(id);
    })
}