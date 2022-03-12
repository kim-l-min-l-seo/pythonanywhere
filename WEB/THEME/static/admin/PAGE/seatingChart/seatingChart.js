// setTimeout("location.reload()",5000)

function select_class() {
	var test = document.getElementById("select_class");
	var select_class = test.options[document.getElementById("select_class").selectedIndex].value;
	
	console.log(select_class);

	// const select_class = document.getElementById("select_class").value;
	console.log('select : ',select_class);
	// seat_init();
	$.ajax({
		type : 'GET',
		url : "seatingChart",
		data : {class_fk : select_class},
		success : function(context) {
			//Console 창으로 data확인
			console.log('데이터 보내기 성공',context.context);
			seatnum_length = context.context.seat_num.length;
			// seat_init();
			var set = []; // 좌석 번호가 담길 좌표 리스트
			for(var i=0; i<column.length; i++) {
				for(var j=0; j<row.length; j++) {				
					set[i*row.length+j]=[i*row.length+j+1,column[i],row[j]]; // set[e] = [좌석번호, x좌표, y좌표]
					// console.log(set[i*row.length+j]);
				}
			}

			seat_on_all(context);
		}//end of success
	})//The end of Ajax
}