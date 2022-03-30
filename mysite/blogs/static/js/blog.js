

const postsBox = document.getElementById('posts-box')

$.ajax({
    type: 'GET',
    url: '/data/',
    success: function (response){
        console.log(response)
        const data = response.data
        console.log(data)

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
                    <a href="" class="btn btn-outline-primary b">Check</a>
                </div>
                <div class="card-footer text-muted text-center mt-3">
                    <strong>Author: ${el.author} |<a href=""></a> Create: ${el.create_on}</strong>
                    <form class="col-6 mx-auto mt-3 text-center" action="" method="post">
                        <a class="btn btn-success"></a>
                        <button class="btn-outline-success btn" type="submit" name="likes">Like</button>
                    </form>
                </div>
           `
        });
    },
    error: function (error){
        console.log(error)

    }
})
