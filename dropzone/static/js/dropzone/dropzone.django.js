// For CORS see https://github.com/enyo/dropzone/issues/33

var djDropzone;

$(function() {

  Dropzone.autoDiscover = false;

  if ($('div.dropzone').length > 0){

    //  Initiate dropzone
    djDropzone = new Dropzone("div.dropzone", {
      url: $(".dropzone").data("upload-path"),
      acceptedFiles: $(".dropzone").data("acceptedfiles"),
      maxFilesize: $(".dropzone").data("maxfilesize")
    });

    var dropzone_url = $("#id_" + djDropzone.element.getAttribute("name"));

    // Add CSRF token to post
    djDropzone.on("sending", function(file, xhr, formData) {
      xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
    });

    // File was successfully uploaded 
    djDropzone.on("success", function(file, response) {
      var file_url = JSON.parse(response)["file_url"];
      dropzone_url.val(dropzone_url.val() + "," + file_url);
    });

    // Show error messages
    djDropzone.on("error", function(file, errorMessage) {
      console.error(errorMessage);
    });

  }

});