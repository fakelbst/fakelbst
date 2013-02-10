
$(document).ready(function(){
    $('.nav li a').click(function(){
        $(this).parent().parent().children().removeClass();
        $(this).parent().addClass('active'); 
    });
});
