(function() {
	$(function() {
		$("div").css("animation-fill-mode", "both");
		$("form").submit(login);
		$("input[type='submit']").blur(removeHint);
	})

	var login = function() {
		if(!$("#number").val() || !$("#password").val()) {
			$("#hint").html("学号和密码不能为空");
			return false;
		}
		$.ajax({
			method:"POST",
			dataType:"json",
			data: $('form').serialize(),
			success: function(json) {

				if(json["state"]) {
					console.log(json['state']);
					window.location.href = json["url"];
				}
				else {
					console.log(json['state']);
					$("#hint").html("学号或密码错误");
				}
			}
		});

		return false;
	}

	var removeHint = function() {
		$("#hint").html("");
	}
})();
