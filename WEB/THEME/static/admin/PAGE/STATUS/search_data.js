
function search_class() {
	var name_classes = document.getElementById("select_class");
	var select_class = name_classes.options[document.getElementById("select_class").selectedIndex].value;
	
	//https://truecode-95.tistory.com/37
	$('input[name=ajax_class_name]').attr('value',select_class)
	//console.log(class_name);

	// const select_class = document.getElementById("select_class").value;
	console.log('select : ', select_class);
	
	$.ajax({
		type : 'GET',

		data : {
			'class_name': select_class,
		},
		success : function(context) {
			//alert(context)
			//Console 창으로 data확인
			console.log('데이터 보내기 성공',context.context);
			$('#ajax_class_name').html(select_class);
		}//end of success
	})//The end of Ajax

}

//https://java119.tistory.com/51
//https://www.python2.net/questions-439716.htm
function tableCreate(){
	var search_late_students = document.getElementById("flexSwitchCheckDefault_late");
	var check_result = search_late_students.getAttribute("checked")
	//var data = list_students.options[document.getElementById("flexSwitchCheckDefault_late").selectedIndex].value;
	
	//Query
	//http://daplus.net/javascript-%EB%B8%8C%EB%9D%BC%EC%9A%B0%EC%A0%80%EC%9D%98-javascript%EC%97%90%EC%84%9C-sql-server-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4%EC%97%90-%EC%97%B0%EA%B2%B0%ED%95%98%EB%8A%94/

	
	$.ajax({
		url: 'status',
		type: 'GET',
		cache: true,
		data : {'class_fk' : select_class},
		success:function(student_list_data){
			var html = '';
			console.log("success");
			//$('#_appendHere').html(data.rendered_table);
			//Console 창으로 data확인
			console.log('데이터 보내기 성공');

			if(document.getElementById("flexSwitchCheckDefault_late").checked){
				console.log('체크~');
			}else{
				console.log('체크해제~');
			}

			for( key in student_list_data ){
			 	html += '<tr>'
			 	html += '<td>' + key+'</td>';
			 	html += '<td>' + student_list_data[key].name+'</td>';
			 	html += '<td>' + student_list_data[key].date+'</td>';
			 	html += '<td>' + student_list_data[key].attendance+'</td>';
			 	html += '<td>' + student_list_data[key].absent+'</td>';
			 	html += '<td>' + student_list_data[key].late+'</td>';
			 	html += '</tr>'
			}

			$("#dynamicTbody").empty();
			$("#dynamicTbody").append(html);
		},
		error: function(data){
			alert("error" + data)
		}
	})
}


//url 기본 통신 확인
$.ajax({
	url: 'data',
	type: "POST",
	dataType: "json",
	data: {'send_data': 'Send this message'},
	success: function(data){
		console.log(data);
	},beforeSend:function(){
		console.log("i am waiting");
	},complete:function(){
		console.log("i am done");
	},error: function (request, status, error) {
		console.log('i am failed');
	}
  });