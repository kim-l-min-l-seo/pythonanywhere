/* 1. jQuery 소개 */
var checkedValue;
var elements = document.getElementsByTagName('input');
for (var n = 0; n < elements.length; n++) {  
    if (elements[n].type == 'radio' &&      
        elements[n].name == 'someRadioGroup' &&      
        elements[n].checked) { 
            checkedValue = elements[n].value;  
        }
    }