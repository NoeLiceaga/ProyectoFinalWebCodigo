window.addEventListener('scroll',function(){
    let head = this.document.querySelector('nav');
    head.classList.toggle('sticky',this.window.scrollY > 0)
    let lista = this.document.querySelectorAll('a')
    lista.forEach(x =>{
        x.classList.toggle('navbar_secondary_color',this.window.scrollY > 0)
    })
})