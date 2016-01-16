$(document).ready(function(){

    $("#close_editor").click(function(){
        $(".editor_frame").fadeOut();
        })

    $('.closeall').click(function(){
        $('.panel-collapse.in')
            .collapse('hide');
        });


    $('.openall').click(function(){
        $('.panel-collapse:not(".in")')
            .collapse('show');
       });

    });