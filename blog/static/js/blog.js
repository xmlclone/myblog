function new_blog() {
    jwt = sessionStorage.getItem('token')
    location.href = `/blog/add?jwt=${jwt}`
}

function save_blog(blog_id) {
    title = $("#title").val()
    if (title.length == 0) {
        alert('标题不能为空')
        return
    }
    body = $("#body").text()
    if (blog_id == "None" || blog_id == undefined) {
        console.log('no blog id')
        axios.post(
            '/api/v1/blog',
            {title, body}
        ).then(resp => {
            if (resp.data.code == 0) {
                // 这里应该跳转到指定blog的页面，也就是后端必须返回创建成功的id
                location.href = "/"
            } 
            // 这里需要增加错误的提示处理
        })
    } else {
        // 更新blog逻辑，建议所有操作都需要登录，比如点赞、收藏等
    }
}