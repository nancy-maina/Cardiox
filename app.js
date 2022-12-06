const user = "user123"
const pass = "user123"

const usernameInputId = "exampleInputUsername"
const passwordInputId = "exampleInputPassword1"

function login() {
    const username = document.getElementById(usernameInputId).value
    const password = document.getElementById(passwordInputId).value

    if (username.trim() === "" || password.trim() === "") {
        alert("Username and password are required!")
        return
    }

    if (username === "user123" && password === "user123") {
        window.location.href = "/start.html"
    } else {
        alert("Invalid username or password")
    }
}

// const menu = document.querySelector('#mobile-menu')
// const menuLinks = document.querySelector('.navbar__menu')

// menu.addEventListener('click', function () {
//     menu.classList.toggle('is-active')
//     menuLinks.classList.toggle('active')
// })

// export default login