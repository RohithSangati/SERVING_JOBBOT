$(function(){
    send_response=function(){
        var val = $("#type_bar").val()      //Here we can take the user input and stores it in val variable
        $.post("message",{message:val})     //We post the user input to 'message' route
        .done(function(response){
            $('#div').append(response);     //after obtaining the response we append it in the message div container
        })
        clear_msg();                        //After that we calls clear_msg function which clears the user input after response and automatic scrolls
    }
    clear_msg=function(){
        $("#type_bar").val("");
        $("html, body").animate({ scrollTop: $(document).height() },1500);
    }
})