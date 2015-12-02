$(document).ready(function(){

    $("#close_editor").click(function(){
        $(".editor_frame").fadeOut();
        })

    $(".card").click(function(){
        $(".editor_frame").fadeIn();
        })
    });