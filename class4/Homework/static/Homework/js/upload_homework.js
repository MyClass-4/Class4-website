// JavaScript Document
window.onload=function(){
	click_able();
	$('.click_able').click(
		function(){
			$('#upload_homework').removeClass('hide_div').addClass('prior_div');
			$('#upload_homework_background').click(
				function(){
					$('#upload_homework').removeClass('prior_div').addClass('hide_div');
					$('#upload_state').text('未提交');
					$('#upload_homework_background').unbind('click');
				}
			);
		}
	);
	$('form').submit(uploadfile);
}

function click_able() {
	$('.is_over').each(function(idx) {
		if ($(this).html() == '未结束')
			$(this).parent().find('.upload').addClass('click_able').html('提交');
	});
}
//上传成功
function upload_success(){
	$('#upload_state').text('上传成功，点击灰色空白处退出');
	$('#upload_homework_background').click(
		function(){
			$('#upload_homework').removeClass('prior_div').addClass('hide_div');
			$('#upload_state').text('未提交');
			$('#upload_homework_background').unbind('click');
		}
	);
}
//上传中
function uploading(){
	$('#upload_homework_background').unbind('click');
	$('#upload_state').text('上传中，请等待');
}
//上传失败
function upload_failed(){
	$('#upload_state').text('上传失败，请点击灰色空白处重来');
	$('#upload_homework_background').click(
		function(){
			$('#upload_homework').removeClass('prior_div').addClass('hide_div');
			$('#upload_state').text('未提交');
			$('#upload_homework_background').unbind('click');
		}
	);
}

var uploadfile = function() {
		if (! /^.+?\\[0-9]{8}\_.+?\.\w+$/.test($('#homework_file').val())) {
			$("#hint").show().text('请输入正确格式：学号_姓名.后缀');
			return　false;
		}
		//var formdata = new FormData();
		// if(!formdata){
		// 	alert('浏览器版本过旧');
		// 	return false;
		// }
		$.ajax({
			method: "POST",
			url: "upload_homework",
			//data: $('#homework_form').serialize(),
			data: new FormData($('#homework_form')[0]),
			processData:false,
 			contentType:false,
			beforeSend: function() {

			},
			success: function(data) {
				if (data["success"])
					upload_success();
			}
		});
		return false;
}
//Ajax这部分是之前的版本加上一个浏览器版本检测，我不知道行不行因为我没找到老版本的浏览器也没有写后端
// function uploadfile(){
// 	$('#homework_form').submit(
//
//
// 			// xhr=$.ajax({
// 			// 	//填写url
// 			// 	url:"",
// 			// 	method:"POST",
// 			// 	data: new FormData($('#homework_form')[0]),
// 			// 	processData:false,
// 			// 	contentType:false,
// 			// 	success: function(data){
// 			// 		if (data.success)
// 			// 			upload_success();
// 			// 	},
// 			// 	beforeSend: function(data){
// 			// 		uploading();
// 			// 	},
// 			// 	error: function(data){
// 			// 		upload_failed();
// 			// 	},
// 			// 	timeout: 300000,
// 			// 	complete: function(xhr,status){
// 			// 		if(status=='timeout'){
// 			// 			upload_failed();
// 			// 		}
// 			// 	}
// 			// });
// 		}
// 	)
// }
