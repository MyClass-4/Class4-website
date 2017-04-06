
$(function() {
  $('form').submit(ajax_submit);
})

var ajax_submit = function() {
  if ($('input[type="text"]').val() == "") return false;
  $.ajax({
      method: "POST",
      dataType: "json",
      data: $('form').serialize(),
      success: function(data) {
        $('#result').text(data);
      }
  })
  return false;
}
