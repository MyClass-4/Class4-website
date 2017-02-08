(function() {
	$(function() {
		$("div").css("animation-fill-mode", "both");
		$("form").submit(login);
		$("input[type='submit']").blur(removeHint);
	})

	var login = function() {
		if($("#number").value() == "" || $("#password").value() == "") {
			$("#hint").html("学号和密码不能为空");
			return false;
		}
		$.ajax({
			method:"POST",
			// url:"/",
			dataType:"json",
			success: function(json) {
				if(json["state"]) {
					window.location.href = json["url"];
				}
				else {
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
