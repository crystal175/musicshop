$(document).ready(function() {
    
    $('#post-form').ajaxForm(function(data) {
        //event.preventDefault();
        console.log("form submitted!");
        $('#resp').html(data);

    });

    $( "#post-form" ).submit(function( event ) {
        var txt = $( "#search-text" ).val();
        $('#search-text').val('');
        console.log(txt);
        //validate field
    });

});

/*$(document).ready(function() {
    
    $('#post-form').on('submit', function(event){
        event.preventDefault();
        console.log("form submitted!");
        go_find();
    });

    function go_find() {
        console.log("go_find is working!");
        console.log($('#search-text').val());
        $.ajax({
            url: "/search/",
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
            },

            error: function(xhr, errmsg, err) {
                $('#resp').html("<p>Error: "+xhr.responseText+" </p>");
                console.log(xhr.status + ": " + xhr.responseText);                
            }
        });
    };

});
*/

/*
$( document ).ready(function() {

    $( "a" ).click(function( event ) {
        event.preventDefault();
        $( this ).hide( "slow" );
    });

    $( "#mus-t" ).on('click', 'tr', function() {
        alert($(this).text());
        var dt = $(this).text();
        console.log(dt);
    });

});
*/
