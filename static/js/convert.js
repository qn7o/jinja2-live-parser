$(document).ready(function(){
    $('#clear').click(function() {
        $('#render').val('');
        $('#values').val('');
        $('#render').html('');
    });

    $('#convert').click(function() {
        var is_checked_showwhitespaces = $('input[name="showwhitespaces"]').is(':checked') ? 1:0;

        // Push the input to the Jinja2 api (Python)
        $.post(window.location, {
            values: $('#values').val(),
            showwhitespaces: is_checked_showwhitespaces
        }).done(function(response) {
            // Grey out the white spaces chars if any
            response = response.replace(/•/g, '<span class="whitespace">•</span>');

            // Display the answer
            $('#render').html(response);
        });
    });
});
