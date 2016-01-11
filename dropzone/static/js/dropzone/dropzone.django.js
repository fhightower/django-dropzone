// For CORS see https://github.com/enyo/dropzone/issues/33

var djDropzones = [];


$(function() {
  var addExistingFiles = function (dropzone, fileUrls) {
    // TODO: It might be wiser to implement this using fake file objects.

    dropzone.loadingExistingFiles = fileUrls;

    var removeLoader = function (fileUrl) {
      var i = dropzone.loadingExistingFiles.indexOf(fileUrl);
      if (i >= 0) {
        dropzone.loadingExistingFiles.splice(i, 1);
      }

      if (dropzone.loadingExistingFiles.length == 0) {
        dropzone.$loadingEl.remove();
      }
    };

    $.each(fileUrls, function(i, fileUrl) {
      var parts = fileUrl.split("/");
      var fileName = parts[parts.length - 1];

      var xhr = new XMLHttpRequest();
      xhr.open("GET", fileUrl);
      xhr.responseType = "blob";
      xhr.onload = function() {
        var file = xhr.response;
        file.upload = {
          progress: 0,
          total: file.size,
          bytesSent: 0
        };
        file.accepted = true;
        file.status = Dropzone.ADDED;
        file.name = fileName;
        file.type = "image/jpeg";
        file.fileUrl = fileUrl;

        dropzone.files.push(file);
        dropzone.emit("addedfile", file);
        dropzone._enqueueThumbnail(file);

        file.status = Dropzone.SUCCESS;
        file.previewElement.classList.add("dz-success");
        file.previewElement.classList.add("dz-complete");
        if (file._removeLink) {
          file._removeLink.textContent = dropzone.options.dictRemoveFile;
        }

        dropzone._updateMaxFilesReachedClass();

        removeLoader(fileUrl);

        return true;
      };
      xhr.send();
    });
  };

  var camelize = function (str) {
    return str.replace(/[\-_](\w)/g, function (match) {
      return match.charAt(1).toUpperCase();
    });
  };

  var djDropzoneEls = $('.djdropzone');

  djDropzoneEls.each(function(i, el) {
    var $el = $(el);
    var dropzoneConfig = $el.data("dropzone-config") || {};
    var fieldName = $el.data("field-name");
    var inputField = $el.parent().find("[name=" + fieldName + "]");
    var $loadingEl = $el.find(".djdropzone-loading");

    $el.addClass("dropzone");

    // Initiate Dropzone
    var dropzone = new Dropzone(el, dropzoneConfig);

    dropzone.$loadingEl = $loadingEl;

    // Add existing files.
    if (inputField.val().length > 0) {
      addExistingFiles(dropzone, inputField.val().split(","));
    }

    // Add CSRF token to post
    dropzone.on("sending", function(file, xhr, formData) {
      xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
    });

    // File was successfully uploaded
    dropzone.on("success", function(file, response) {
      if (response) {
        var fileUrl = JSON.parse(response)["file_url"];
        file.fileUrl = fileUrl;

        var val = inputField.val();
        var fileUrls = val.length > 0 ? val.split(",") : [];

        if (fileUrls.indexOf(fileUrl) < 1) {
          fileUrls.push(fileUrl);
        }

        inputField.val(fileUrls.join());
      }
    });

    // Show error messages
    dropzone.on("error", function(file, errorMessage) {
      console.error(errorMessage);
    });

    dropzone.on("removedfile", function(file) {
      var fileUrl = file.fileUrl;
      var fileUrls = inputField.val().split(",");

      var i = fileUrls.indexOf(fileUrl);
      if (i >= 0) {
        fileUrls.splice(i, 1);
      }

      inputField.val(fileUrls.join());
    });

    djDropzones.push(dropzone);

    Dropzone.options[camelize(el.id)] = false;

  });

});
