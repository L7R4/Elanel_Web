const url = window.location.pathname


// HEADER
if (url == "/admin/market/beneficioparacliente/" || 
    url == "/admin/market/cliente/" ||
    url == "/admin/market/electrodomestico/" ||
    url == "/admin/market/moto/" ||
    url == "/admin/market/numadjudicado/" ||
    url == "/admin/market/personal/" ||
    url == "/admin/market/post/" ||
    url == "/admin/market/soluciondineraria/" ||
    url == "/admin/auth/user/" ||
    url == "/admin/auth/group/" 
    )
{
    reoderHeader()
}

if (url == "/admin/market/cliente/" ||
    url == "/admin/market/personal/" ||
    url == "/admin/market/beneficioparacliente/" 
    ) 
{
    removeButtonAdd_and_reoderButtons()
}

// -----------------


// PANEL DE CONTROL

let q = document.querySelector(".container>.row")   

if (url == "/admin/") {
    let x = document.querySelector(".container-fluid > .row > div:nth-child(1)")
    let a = document.querySelector(".container-fluid > .row > div:nth-child(2)")
    x.classList.remove("col-12", "col-md-auto" ,"d-flex" ,"flex-grow-1", "align-items-center")
    
    let b = document.querySelector(".container-fluid > .content > .row > div:nth-child(1)")
    let c = document.querySelector(".container-fluid > .content > .row > div:nth-child(2)")

    c.classList.remove("col-lg-3" ,"col-12")
    c.setAttribute("style", "width:100%")

    b.classList.remove("col-lg-9", "col-12")
    b.setAttribute("style", "width:100%")


}

// ---------------------







function reoderHeader() {
    let x = document.querySelector(".container-fluid > .row > div:nth-child(1)")
    let a = document.querySelector(".container-fluid > .row > div:nth-child(2)")
    x.classList.remove("col-12", "col-md-auto" ,"d-flex" ,"flex-grow-1", "align-items-center")
    a.classList.remove("col-12" ,"col-md-auto" ,"d-flex" ,"align-items-center" ,"justify-content-end" ,"page-actions")
}

function removeButtonAdd_and_reoderButtons() {
    let button_add_client = document.querySelector(".btn.btn-success.float-right")
    button_add_client.classList.add("hidden")
    let container_buttons_imports = document.querySelector(".btn-group.float-right")
    container_buttons_imports.classList.add("gap_for_flex")
}