$(document).ready(function(){

//////////////////Motor Functions///////////////////////
$("#MOTORup").mousehold(300,function(i){
$.get(document.URL + "up");
});

$("#MOTORdown").mousehold(300,function(i){
$.get(document.URL + "down");
});

$("#MOTORleft").mousehold(300,function(i){
$.get(document.URL + "left");
});

$("#MOTORright").mousehold(300,function(i){
$.get(document.URL + "right");
});


$("#MOTORforward").mousehold(300,function(i){
$.get(document.URL + "forward");
});


$("#MOTORstop").mousehold(300,function(i){
$.get(document.URL + "stop");
});


});

