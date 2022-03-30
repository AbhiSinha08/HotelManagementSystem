const tables = {
    rooms: document.getElementById('rooms'),
    reservations: document.getElementById('reservations'),
    customers: document.getElementById('customers'),
    employees: document.getElementById('employees')
};

function showTable(name) {
    for (var table of Object.values(tables))
        table.classList.add('hidden');
    tables[name].classList.remove('hidden');
}

async function tranDetails(id) {
    url = "/t?id=" + id;
    let details = await (await fetch(url)).json();
    if (details.status == 1)
        var status = "Success";
    else if (details.status == 0)
        var status = "Pending";
    else var status = "Declined";
    const message = `Transaction ID: ${id}
    Date: ${details.date}
    Amount: ${details.amount}
    Payment Mode: ${details.payment}
    Payment Status: ${status}`;
    alert(message);
}

const buttons = {
    rooms: tables.rooms.querySelectorAll("button"),
    reservations: tables.reservations.querySelectorAll("button"),
    customers: tables.customers.querySelectorAll("button"),
    employees: tables.employees.querySelectorAll("button")
};

for (var btn of buttons.rooms) {
    if (btn.getAttribute("data-type") == "delete") {
        const id = btn.getAttribute("data-id");
        btn.addEventListener("click", () => {
            window.location.href = "/del/room?id=" + id;
        })
    }
}

for (var btn of buttons.reservations) {
    if (btn.getAttribute("data-type") == "delete") {
        const id = btn.getAttribute("data-id");
        btn.addEventListener("click", () => {
            window.location.href = "/del/res?id=" + id;
        })
    }
}

for (var btn of buttons.customers) {
    if (btn.getAttribute("data-type") == "delete") {
        const id = btn.getAttribute("data-id");
        btn.addEventListener("click", () => {
            window.location.href = "/del/cust?id=" + id;
        })
    }
}

for (var btn of buttons.employees) {
    if (btn.getAttribute("data-type") == "delete") {
        const id = btn.getAttribute("data-id");
        btn.addEventListener("click", () => {
            window.location.href = "/del/emp?id=" + id;
        })
    }
}

const clearBtn = document.getElementById("clear");
clearBtn.addEventListener('click', () => {
    if (confirm("Clear The Entire Database?")) {
        window.location.href = '/clear';
    }
})