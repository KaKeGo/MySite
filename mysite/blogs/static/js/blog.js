
const spinnerBox = document.getElementById('spinner-box')


$.ajax({
    type: 'GET',
    url: '/data/',
    success: function (response){
        console.log(response)

    },
    error: function (error){
        console.log(error)
    }
})
