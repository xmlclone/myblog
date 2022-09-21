function redirect_login() {
    location.href = '/login'
}

function redirect_resiger() {
    location.href = '/register'
}

function register() {
    username = $('#username').val().trim()
    password1 = $('#password1').val().trim()
    password2 = $('#password2').val().trim()
    info = null
    alter_ele = $('#register-alter')
    if (username.length == 0) {
        info = '用户名不能为空'
    }
    if ((password1.length == 0) || (password2.length == 0)) {
        info = '密码不能为空'
    } else {
        if (password1 != password2) {
            info = '两次密码不一样'
        }
    }
    if (info != null) {
        // addClass是增加
        // attr是直接覆盖
        alter_ele.attr('class', 'text-warning')
        alter_ele.text(info)
        return
    }
    password = password1
    axios.post(
        '/api/v1/auth/register',
        {
            username,
            password
        }
    ).then(resp => {
        if (resp.data.code != 0) {
            alter_ele.attr('class', 'text-warning')
            alter_ele.text(resp.data.message)
        } else {
            alter_ele.attr('class', 'text-info')
            alter_ele.text('注册成功，稍后跳转到登录页面')
            setTimeout(() => {location.href='/login'}, 1000)
        }
    })
}

function login() {
    username = $('#username').val().trim()
    password = $('#password').val().trim()
    alter_ele = $('#login-alter')
    info = null
    if (username.length == 0) {
        info = '用户名不能为空'
    }
    if (password.length == 0) {
        info = '密码不能为空'
    }
    if (info != null) {
        alter_ele.attr('class', 'text-warning')
        alter_ele.text(info)
        return
    }
    axios.post(
        '/api/v1/auth/token',
        {
            username,
            password
        }
    ).then(resp => {
        if (resp.data.code != 0) {
            alter_ele.attr('class', 'text-warning')
            alter_ele.text(resp.data.message)
        } else {
            alter_ele.attr('class', 'text-info')
            alter_ele.text('登录成功，稍后跳转到首页')
            console.log(`Token is: ${resp.data.token}`)
            document.cookie = `token=${resp.data.token}`
        }
    })
}