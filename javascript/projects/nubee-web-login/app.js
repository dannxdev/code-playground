function iniciarSesionButton() {

    let dbUser = "dannxdev"
    let dbPassword = "752194"

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
