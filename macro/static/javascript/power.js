$(document).ready(function(event){

    $("#cb_power").click( function(){
        if ($("#cb_power").attr("checked") == "checked"){
            $("#cbt_power").val('on');
        }
        else{
            $("#cbt_power").val('off');
            $("#cb_power").attr("disabled", "disabled");
            $(this).closest("form").submit();
        }
    });

});