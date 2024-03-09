
$(document).ready(function() {
    $('#prompt-form').submit(function(event) {
        event.preventDefault(); // Prevent form submission
        var prompt = $('#prompt').val();
        $.post('/generate', {prompt: prompt}, function(response) {
            $('#generated-text').text(response);
        });
    });
});
