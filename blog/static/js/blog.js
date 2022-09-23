function new_blog() {
    jwt = sessionStorage.getItem('token')
    location.href = `/blog/add?jwt=${jwt}`
}

function edit_blog(blog_id) {
    jwt = sessionStorage.getItem('token')
    location.href = `/blog/update/${blog_id}?jwt=${jwt}`
}

function delete_blog(blog_id) {
    c = confirm("确认删除？")
    if (c!=true) {
        return
    }
    axios.delete(`/api/v1/blog/${blog_id}`).then(resp => {
        if (resp.data.code != 0) {
            console.log(resp)
            alert('删除失败')
        } else {
            // 需要给与提示
            location.href = '/'
        }
    }).catch(err => {
        console.log(err)
        alert('删除失败')
    })
}

function save_blog(blog_id) {
    title = $("#title").val()
    if (title.length == 0) {
        alert('标题不能为空')
        return
    }
    body = $("#body").text()
    if (blog_id == "None" || blog_id == undefined) {
        // 新建blog逻辑
        console.log('no blog id')
        axios.post(
            '/api/v1/blog',
            {title, body}
        ).then(resp => {
            if (resp.data.code == 0) {
                // 这里应该跳转到指定blog的页面，也就是后端必须返回创建成功的id
                location.href = "/blog/view/"
            } 
            // 这里需要增加错误的提示处理
        })
    } else {
        // 更新blog逻辑，建议所有操作都需要登录，比如点赞、收藏等
        axios.put(
            `/api/v1/blog/${blog_id}`,
            {title, body}
        ).then(resp => {
            if (resp.data.code != 0) {
                console.log('更新失败')
            } else {
                location.href = `/blog/view/${blog_id}`
            }
        })
    }
}