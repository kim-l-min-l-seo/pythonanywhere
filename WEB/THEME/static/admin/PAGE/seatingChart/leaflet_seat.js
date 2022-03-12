// 기본설정
var map = L.map('map', {crs: L.CRS.Simple, zoomControl: false, maxZoom: 0, dragging: false});
var imgurl = '/static/PAGE/seatingChart/seatingChart4.jpg' // 이미지 경로
var bounds = [[0,0], [680,1500]]; // 이미지의 해상도를 bounds로 설정한다. [y,x]
L.imageOverlay( imgurl, bounds).addTo(map); // 배경 이미지를 설정한다.
// 얘는 냅둘것
map.fitBounds(bounds); // 표현 영역을 설정한다

// 좌표 설정
const column = [143,373,603,833,1063,1293]; // 분단 x 좌표
const row = [160,285,410,535,650]; // 몇번째 자리인지 y 좌표
var set = []; // 좌석 번호가 담길 좌표 리스트
for(var i=0; i<column.length; i++) {
	for(var j=0; j<row.length; j++) {				
		set[i*row.length+j]=[i*row.length+j+1,column[i],row[j]]; // set[e] = [좌석번호, x좌표, y좌표]
		// console.log(set[i*row.length+j]);
	}
}
// const column = [138,317,496,675,854,1033,1212,1391]; // 분단 x 좌표
// const row = [253,375,498,620]; // 몇번째 자리인지 y 좌표
// var set = []; // 좌석 번호가 담길 좌표 리스트
// for(var i=0; i<column.length; i++) {
// 	for(var j=0; j<row.length; j++) {				
// 		set[i*row.length+j]=[i*row.length+j+1,column[i],row[j]]; // set[e] = [좌석번호, x좌표, y좌표]
// 		// console.log(set[i*row.length+j]);
// 	}
// }

const color = ['green','red','orange','gray'];
// 출 결 지 조 색깔

function seat_on(seat_num, select_class, nameValue, majorValue, daily_info,state,emailValue) {
	var name='"'+nameValue+'"';
	var class_name='"'+select_class+'"';
	var major='"'+majorValue+'"';
	var temperature=daily_info[1];
	var email=emailValue;
	var url = "'/static/img/avatars/"+email+".jpg'";
	var img_url = "<img src="+url+">";
	var color_name = color[state];
	var popup_content = new L.Rrose({ autoPan: false, offset: new L.Point(0,-10), closeButton: false })
	.setContent("<center>"+name+"</center><br />"+img_url+"<br />\
	<br /><center>반 : "+class_name+" 반</center><br />\
	<center>전공 : "+major+"</center><br />\
	<center>체온 : "+temperature+" 도</center>");

	L.circle([set[seat_num-1][2], set[seat_num-1][1]], {color: color_name, radius: 23, fillOpacity: 1}).addTo(map)
	.bindTooltip(name, {permanent: true, direction: 'center', opacity: 1}).openTooltip()
	.bindPopup(popup_content)
	.on("mouseover", function(evt) { this.openPopup(); })
	.on("mouseout", function(evt) { this.closePopup(); });
}

function seat_on_all(context){
	for(var i=0; i<seatnum_length; i++){
		try{
			nameValue = context.context.name[i];
			classValue = context.context.class_name[i];
			majorValue = context.context.major[i];
			seatnumValue = context.context.seat_num[i];
			daily_info_Value = context.context.daily_info[i];
			input_time_Value = context.context.daily_info[i][0];
			state = context.context.daily_info[i].slice(2).lastIndexOf('Y');
			emailValue = context.context.email[i];

			console.log("seat_on"+i);
			// remove_async();
			seat_on(seatnumValue, classValue, nameValue, majorValue, daily_info_Value,state,emailValue);
		} catch(error) { 
			console.log(error); 
		}
	}
}

async function seat_final(context){
	try {
		let message = await seat_reset();
		console.log(message);
		if (message == "success") {
			seat_init();
			seat_on_all(context);
		}
	} catch (error) {
		console.log(error);
	}
	
}

// async function remove_async(el) {
// 	var parent = await el.parentNode;
// 	if (parent) {
// 		parent.removeChild(el);
// 		console.log("remove_new");
//   }
// }

function seat_init() {
	// location.reload();
	// seat_reset();
	var map = L.map('map', {crs: L.CRS.Simple, zoomControl: false, maxZoom: 0, dragging: false});
	var imgurl = '/static/PAGE/seatingChart/seatingChart.jpg' // 이미지 경로
	var bounds = [[0,0], [680,1500]]; // 이미지의 해상도를 bounds로 설정한다. [y,x]
	L.imageOverlay( imgurl, bounds).addTo(map); // 배경 이미지를 설정한다.
	map.fitBounds(bounds); // 표현 영역을 설정한다
}

function seat_reset() {
	return new Promise(function(resolve,reject){
		map.remove_async();
		resolve("success");
	});
}