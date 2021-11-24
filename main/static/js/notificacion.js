document.getElementById('form').addEventListener('submit',checo)

function showNotificacion(){
    const notificacion = new Notification("Mensaje De ProyectoWeb",{
        body: "Nueva propuesta de empleo agregada"
    })
}

function checo(){
    console.log(Notification.permission)

    if(Notification.permission === 'granted'){
        showNotificacion()
    
    }else if(Notification.permission !== 'denied'){
        Notification.requestPermission().then(permission => {
            if(permission ==='granted'){
                showNotificacion()
            }
        })
    }
}
