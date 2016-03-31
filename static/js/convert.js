$(document).ready(function(){
    $('#clear').click(function() {
        $('#template').val('');
        $('#render').val('');
        $('#values').val('');
        $('#render').html('');
    });

    // $('#use_yaml').click(function() {
    $('input[type=checkbox]').change(function() {
        if($(this).is(':checked')) {
            $("#data h1").html("Values (YAML)");
        }
        else {
            $("#data h1").html("Values (JSON)");
        } 
    });

    $('#convert').click(function() {
        var is_checked_showwhitespaces = $('input[name="showwhitespaces"]').is(':checked') ? 1:0;
        var is_checked_dummyvalues = $('input[name="dummyvalues"]').is(':checked') ? 1:0;
        var is_checked_use_yaml = $('input[name="use_yaml"]').is(':checked') ? 1:0;


        // Push the input to the Jinja2 api (Python)
        $.post('/convert', {
            template: $('#template').val(),
            values: $('#values').val(),
            showwhitespaces: is_checked_showwhitespaces,
            dummyvalues: is_checked_dummyvalues,
            use_yaml: is_checked_use_yaml
        }).done(function(response) {
            // Grey out the white spaces chars if any
            response = response.replace(/•/g, '<span class="whitespace">•</span>');

            // Display the answer
            $('#render').html(response);
        });
    });
});
