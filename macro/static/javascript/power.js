$(document).ready(function(event){

    $("#cb_power").click( function(){
        if ($("#cb_power").attr("checked") == "checked"){
            $("#cbt_power").val('on');
        }
        else{
            $("#cbt_power").val('off');
            $("#cb_power").attr("disabled", "disabled");
            //$(this).closest("form").submit();
            $.ajax({
                url: '/macro/settings/power/',
                type: 'POST',
                data: {
                    command : "off",
                    csrfmiddlewaretoken: token,
                },
                success: function (ret)
                {
                    $('#status').html(ret).removeClass('hidden');
                    
                }
            });
        }
    });

});