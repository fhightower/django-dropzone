// For CORS see https://github.com/enyo/dropzone/issues/33

var djDropzones = [];

$(function() {
  var djDropzoneEls = $('.djdropzone');

  djDropzoneEls.each(function(i, el) {
    var $el = $(el);
    var dropzoneConfig = $el.data("dropzone-config") || {};
    var fieldName = $el.data("field-name");
    var inputField = $el.parent().find("[name=" + fieldName + "]");

    $el.addClass("dropzone");

    // Initiate Dropzone
    var dropzone = new Dropzone(el, dropzoneConfig);

    // Add CSRF token to post
    dropzone.on("sending", function(file, xhr, formData) {
      xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
    });

    // File was successfully uploaded
    dropzone.on("success", function(file, response) {
      var file_url = JSON.parse(response)["file_url"];
      inputField.val(inputField.val() + "," + file_url);
    });

    // Show error messages
    dropzone.on("error", function(file, errorMessage) {
      console.error(errorMessage);
    });

    djDropzones.push(dropzone);

  });

});
