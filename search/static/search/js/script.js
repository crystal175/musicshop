$(document).ready(function() {
    
    $('#post-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!");
        go_find();
    });

    function go_find() {
        console.log("go_find is working!");
        console.log($('#search-text').val());
        $.ajax({
            url: "/search/hello/",
            type: "POST",
            data: {
                search_text: $('#search-text').val(),
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },

            success: function(json) {
                $('#search-text').val('');
                //console.log(json);
                console.log("success");
                
                // render template on django 
                $('#resp').html(json);


                // 2 plain res
                //$('#resp').append(json+"<br>")

                // 1 json
                //for (js in json) {
                //    console.log(js);
                //    $('#resp').prepend(js + "<br>");
                //}
                //$('#resp').append("<p>"+json+"</p>")
            },

            error: function(xhr, errmsg, err) {
                $('#resp').html("<p>Error: "+xhr.responseText+" </p>");
                console.log(xhr.status + ": " + xhr.responseText);                
            }
        });
    };

});
