// CSRF Cookie for AJAX: https://docs.djangoproject.com/en/1.5/ref/contrib/csrf/#ajax

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = ordering.jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var csrftoken = getCookie("csrftoken");

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}

ordering.jQuery.ajaxSetup({
  crossDomain: false, // obviates need for sameOrigin test
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type)) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  },
});
