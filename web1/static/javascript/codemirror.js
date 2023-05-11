var editor = CodeMirror.fromTextArea(document.getElementById("my-textarea"), {
    mode: "python",
    lineNumbers: true,
    theme: "default",
});
$(function() {
    $('form').submit(function(event) {
      event.preventDefault();
  
      $.ajax({
        type: 'POST',
        url: '/',
        data: $('form').serialize(),
        success: function(response) {
          $('#output').text(response.output);
        },
        error: function(response) {
          alert('An error occurred while executing the code.');
        }
      });
    });
  });
  