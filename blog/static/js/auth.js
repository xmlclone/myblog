function redirect_login() {
    location.href = '/login'
}

function redirect_resiger() {
    location.href = '/register'
}

function logout_helper() {
    $("#login").show()
    $("#register").show()
    $("#username").show()
    $("#logout").hide()
    $("#new").hide()
    sessionStorage.clear()
}

function logout() {
    logout_helper()
    location.href = '/'
}