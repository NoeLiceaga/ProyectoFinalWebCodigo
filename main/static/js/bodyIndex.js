
let contenedor =  document.getElementById('categoria_total')
let url = document.URL;
let colores = [
    "#007bff",
    "#6610f2",
    "#6f42c1",
    "#e83e8c",
    "#dc3545",
    "#fd7e14",
    "#ffc107",
    "#28a745",
    "#20c997",
    "#17a2b8",
    "#dc3545",
    "#ffc107"
]
let categorias = [
    "Contabilidad y Administración",
    "Comunicaciones",
    "Construcción y edificación",
    "Diseño",
    "Derecho y leyes",
    "Educación",
    "Ingeniería",
    "Manufactura",
    "Mercadotecnia",
    "Salud",
    "Tecnología de la Información",
    "Zoología"
]
let clasesIcono= [
    "bx-dollar",
    "bx-receipt",
    "bx-buildings",
    "bxs-droplet-half",
    "bxs-hand",
    "bxs-happy",
    "bx-brain",
    "bxs-cuboid",
    "bx-paper-plane",
    "bxs-ambulance",
    "bx-code-alt",
    "bx-bug-alt"
]
const cargaCategorias = () =>{
    let i=0
    categorias.forEach(x =>{
        let ic = clasesIcono[i]
        let icono = document.createElement('i')
        let h1 = document.createElement('h1')
        let div = document.createElement('div')
        icono.classList.add('bx')
        icono.classList.add(ic)
        h1.innerHTML = x
        div.appendChild(icono)
        div.appendChild(h1)
        div.style.backgroundColor = colores[i]
        div.classList.add('categoria_total_elemento')
        contenedor.appendChild(div)
        i++
    })


}
const creaPanelPersona = () =>{
    for(let i=0; i<3; i++){
        let imagenes = ["https://www.uandes.cl/wp-content/uploads/2019/01/solange-contreras-direccion-de-personas-uandes-1.jpg",
        "https://www.superprof.mx/imagenes/anuncios/profesor-home-persona-seria-formal-con-experiencia-mas-anos-residiendo-trabajando-inglaterra-ofrece-para-dar-apoyo.jpg",
        "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/gettyimages-736512991-1588575246.jpg?crop=1xw:1xh;center,top&resize=640:*"]
        let nombre =["Leticia","Ruben","Martina"];
        let abuelo = document.getElementById('solictante_info')
        let padre = document.createElement('div')
        let imagen = document.createElement('img')
        let div = document.createElement('div')
        let divImg = document.createElement('div')
        let icon1  = document.createElement('i')
        let icon2 = document.createElement('i')
        let p = document.createElement('p')
        let h4 = document.createElement('h4')
        let parrafo = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Dignissimos iste tempora facere doloremque molestias vitae nisi repellendus officia quis non?"
        imagen.src =imagenes[i]
        divImg.appendChild(imagen)
        divImg.classList.add('img')
    
        div.classList.add('info')
        icon1.classList.add('bx')
        icon1.classList.add('bxs-quote-single-left')
        icon2.classList.add('bx')
        icon2.classList.add('bxs-quote-single-right')
        p.innerHTML = parrafo
        h4.innerHTML = nombre[i]
        div.appendChild(icon1)
        div.appendChild(icon2)
        div.appendChild(p)
        div.appendChild(h4)
        padre.appendChild(divImg)
        padre.appendChild(div)
        padre.classList.add('solicitante_info_contenedor')
        abuelo.appendChild(padre)
    }
}
cargaCategorias()
creaPanelPersona()