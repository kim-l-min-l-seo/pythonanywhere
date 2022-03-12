document.addEventListener("DOMContentLoaded", function() {

    notice({

          uniqueid : "notice"

        , style : {

             "padding" : "2px"

            , "width" : "600px"

            , "height" : "30px"

        }

        , inc : 5                              // 속도

        , mouse : "cursor driven"       // 마우스 사용여부

        , moveatleast : 2                  // 이동속도

        , neutral : 150

        , savedirection : true             // false를 선언하면 마우스 커서가 위치하는 순간 역방향으로 움직인다.

        , random : false                   // 나오는 순서(기본값 : true)

    });

})