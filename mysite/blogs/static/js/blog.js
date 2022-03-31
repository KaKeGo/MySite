

const spinnerBox = document.getElementById('spinner-box')
const postsBox = document.getElementById('posts-box')
const moreBlogsBox = document.getElementById('more-blogs')
const loadBtnBox = document.getElementById('load-btn')

const detailUrl = window.location.href

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

const likeUnlikePosts = () => {
    const likeUnlikeForms = [...document.getElementsByClassName('like-unlike-forms')]
    likeUnlikeForms.forEach(form=> form.addEventListener('submit', e=>{
        e.preventDefault()
        const clickerId = e.target.getAttribute('data-form-id')
        const clickedBtn = document.getElementById(`like-unlike-${clickerId}`)

        $.ajax({
            type: 'POST',
            url: '/like-unlike/',
            data: {
                'csrfmiddlewaretoken': csrftoken,
                'pk': clickerId,
            },
            success: function (response){
                console.log(response)
                clickedBtn.innerHTML = `${response.count}
                                ${response.likes ?
                                `Unlike`: 
                                `Like`
                                }`
            },
            error: function (error){
                console.log(error)
            }
        })
    }))
}

let visible = 3

const getData = () => {
    $.ajax({
        type: 'GET',
        url: `/data/${visible}`,
        success: function (response){
            console.log(response)
            const data = response.data
            setTimeout(()=>{
                spinnerBox.classList.add('not-visible')
                data.forEach(el=> {
                   postsBox.innerHTML += `
                      <div class="card-body">
                          <hr/>
                        <div class="text-center mt-2">
                            <h5 class="card-title">${el.title}</h5>
                        </div>
                        <hr/>
                        <div class="mx-5">
                            <p class="card-text">${el.body}</p>
                        </div>
                        <div class="d-grip gap-2 col-6 mx-auto row mt-3">
                            <a href="${detailUrl}detail/${el.slug}" class="btn btn-outline-primary b">Check</a>
                        </div>
                        <div class="card-footer text-muted text-center mt-3">
                            <strong>Author: ${el.author} |<a href=""></a> Create: ${el.create_on}</strong>
                            <br/>
                            <form class="col-lg-3 mx-auto mt-3 text-center btn-group like-unlike-forms" data-form-id="${el.id}" method="post">
                                <a class="btn btn-success not-visible">${el.count}</a>
                                ${el.likes ?
                                `<button class="col-lg-4 btn-outline-danger btn hidden" type="submit" id="like-unlike-${el.id }name="likes">Unlike`: 
                                `<button class="btn-outline-success btn hidden" type="submit" name="likes" id="like-unlike-${el.id}">Like</button>`
                                }
                            </form>
                        </div>
                   `
                });
                likeUnlikePosts()
            }, 100)
            console.log(response.size)
            if (response.size === 0) {
                moreBlogsBox.innerHTML = `
                    <hr/>
                    <strong>Eny blog not added yet</strong>`
            }
            else if (response.size <= visible) {
                loadBtnBox.classList.add('not-visible')
                moreBlogsBox.innerHTML = `
                    <hr/>
                    <strong>No more blogs</strong>`
            }
        },
        error: function (error){
            console.log(error)

        }
    })
}

loadBtnBox.addEventListener('click', () =>{
    spinnerBox.classList.remove('not-visible')
    visible += 3
    getData()
})

getData()
