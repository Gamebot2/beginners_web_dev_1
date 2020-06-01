function sendRequest() {

    $.ajax({
        type: 'GET',
        url: "/example",
        success: function(data) {
            document.getElementById("response").innerHTML = data;
        }
    })

}