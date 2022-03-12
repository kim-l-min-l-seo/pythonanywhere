// setTimeout("location.reload()",5000)
$.ajax({
	type : 'GET',
	url : "total_member",
	// data : {test : ''},
	success : function(count) {
		//Console 창으로 data확인
		console.log('데이터 보내기 성공',count);

		// const total = document.getElementById("total_member");
		// total.innerText = count.total

		const attendance = document.getElementById("total_attendance");
		attendance.innerText = count.attendance+' / '+count.total

		const absent = document.getElementById("total_absent");
		absent.innerText = count.absent+' / '+count.total

		const late = document.getElementById("total_late");
		late.innerText = count.late+' / '+count.total

		const early = document.getElementById("total_early");
		early.innerText = count.early+' / '+count.total
	
		// $('#test').load(window.location.href + '#test');
	}//end of success
})//The end of Ajax

/*
$.ajax({
	type : 'GET',
	url : "total_attendance",
	// data : {test : ''},
	success : function(count) {
		//Console 창으로 data확인
		console.log('데이터 보내기 성공',count);

		const value = document.getElementById("total_attendance");
		value.innerText = count.count
	
		// $('#test').load(window.location.href + '#test');
	}//end of success
})//The end of Ajax

$.ajax({
	type : 'GET',
	url : "total_absent",
	// data : {test : ''},
	success : function(count) {
		//Console 창으로 data확인
		console.log('데이터 보내기 성공',count);

		const value = document.getElementById("total_absent");
		value.innerText = count.count
	}//end of success
})//The end of Ajax

$.ajax({
	type : 'GET',
	url : "total_late",
	// data : {test : ''},
	success : function(count) {
		//Console 창으로 data확인
		console.log('데이터 보내기 성공',count);

		const value = document.getElementById("total_late");
		value.innerText = count.count
	}//end of success
})//The end of Ajax

$.ajax({
	type : 'GET',
	url : "total_early",
	// data : {test : ''},
	success : function(count) {
		//Console 창으로 data확인
		console.log('데이터 보내기 성공',count);

		const value = document.getElementById("total_early");
		value.innerText = count.count
	}//end of success
})//The end of Ajax
*/



function select_class() {
	var test = document.getElementById("select_class");
	var select_class = test.options[document.getElementById("select_class").selectedIndex].value;
	console.log('select : ',select_class)
	$.ajax({
		type : 'GET',
		url : "class_statistics",
		data : {class_fk : select_class},
		success : function(context) {
			//Console 창으로 data확인
			// console.log('데이터 보내기 성공',context.context);

			attendanceValue = context.context.attendance
			absentValue = context.context.absent
			lateValue = context.context.late
			earlyValue = context.context.early
			totalCountMember = context.context.totalCountMember

			//전광판에 반 출결지조 데이터 삽입
			const attendanceTag = document.getElementById("class_attendance");
			attendanceTag.innerText = attendanceValue
			// attendanceTag.innerText = attendanceValue+' / '+totalCountMember

			const absentTag = document.getElementById("class_absent");
			absentTag.innerText = absentValue
			// absentTag.innerText = absentValue+' / '+totalCountMember

			const lateTag = document.getElementById("class_late");
			lateTag.innerText = lateValue
			// lateTag.innerText = lateValue+' / '+totalCountMember

			const earlyTag = document.getElementById("class_early");
			earlyTag.innerText = earlyValue
			// earlyTag.innerText = earlyValue+' / '+totalCountMember

			//HIDDEN INPUT 태그에 데이터 삽입
			
			new Chart(document.getElementById("chartjs-dashboard-bar"), {
		

				type: "bar",
				data: {
					labels: ["출석", "결석", "지각", "조퇴"],
					datasets: [{
						label: "오늘",
						backgroundColor: window.theme.warning,
						borderColor: window.theme.danger,
						hoverBackgroundColor: window.theme.success,
						hoverBorderColor: window.theme.primary,
						data: [
							document.getElementById("class_attendance").innerText, 
							document.getElementById("class_absent").innerText, 
							document.getElementById("class_late").innerText, 
							document.getElementById("class_early").innerText
						],
						// data: [100, 50, 70, 80],
						barPercentage: .75,
						categoryPercentage: .5
					}]
				},
				options: {
					maintainAspectRatio: false,
					legend: {
						display: false
					},
					scales: {
						yAxes: [{
							gridLines: {
								display: false
							},
							stacked: false,
							ticks: {
								stepSize: 20
							}
						}],
						xAxes: [{
							stacked: false,
							gridLines: {
								color: "transparent"
							}
						}]
					}
				}
			}); // The end of Chart

		}//end of success
	})//The end of Ajax

}


document.addEventListener("DOMContentLoaded", function () {
	// Bar chart
		console.log("출석 :")
		console.log("결석 :")
		console.log("지각 :")
		console.log("조퇴 :")
	
});