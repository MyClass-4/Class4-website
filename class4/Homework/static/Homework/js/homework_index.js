// JavaScript Document
window.onload=function(){
	$('form').submit(uploadfile);
}

var uploadfile = function() {
		// if (! /^.+?\\[0-9]{8}\_.+?\.\w+$/.test($('#homework_file').val())) {
		// 	$("#hint").show().text('请输入正确格式：学号_姓名.后缀');
		// 	return　false;
		// }
		var formdata = new FormData($(this)[0]);
		formdata.append('course_name', $(this).parent().find('#course_name').html());
		formdata.append('homework_name', $(this).parent().find('#homework_name').html());
		$.ajax({
			method: "POST",
			url: "upload_homework",
			data: formdata,
			processData:false,
 			contentType:false,
			beforeSend: function() {

			},
			success: function(data) {
				if (data["success"])
					$('.hint').html('提交成功');
			}
		});
		return false;
}
