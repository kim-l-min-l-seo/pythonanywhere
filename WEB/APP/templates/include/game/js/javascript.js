<script>
    
    function youtube_url(){
    
        var dataUrl = $('#search-input').val();
        
        console.log(dataUrl)

        $.ajax({
            url:'/down/mosic/url/',  //request 보낼 서버의 경로
            type:'post',            // 메소드(get, post, put 등)
            data:{'dataUrl':dataUrl},       //보낼 데이터
            success: function(data) {
                //서버로부터 정상적으로 응답이 왔을 때 실행
                console.log("data : ",data)
            },
            error: function(err) {
                //서버로부터 응답이 정상적으로 처리되지 못햇을 때 실행
            }
        });

    }// The end of method

</script>