function iniciarSesionButton() {

    let dbUser = "danielb21"
    let dbPassword = "daniel752194"

    let username = document.getElementById("username").value
    let userPassword = document.getElementById("password").value
    
    if (dbUser == username) {
        // El nombre de usuario es correcto:
        if (dbPassword == userPassword) {
            alert("Haz iniciado sesion.")
        } else {
            alert("La contraseña es incorrecta.")
        }

    } else {
        alert("ERROR: El usuario no existe.")
    }
}
