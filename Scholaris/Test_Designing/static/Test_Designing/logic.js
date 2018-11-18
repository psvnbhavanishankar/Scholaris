$(function(){
    var current_qs =1;
    var qs_attempted;
    var percentage = 0;

    console.log($(".qs-text").value)
    progress(percentage);
    $('.carousel').carousel('pause')

    $("#prev").click(function(){
        if(get_current() != 1) {
            $('.carousel').carousel('prev')
        }
    });

    $("#next").click(function(){
        if(get_current() != 10) {
            $('.carousel').carousel('next')
        }
        else{
            window.alert("Its the last question! Please click Submit")
        }
    });

    $(".carousel-item").first().addClass("active")

    $('input[type=radio]').click(function () {
        qs_attempted = $(':radio:checked');
        console.log(qs_attempted)
        //console.log(number);
        percentage = (qs_attempted.length *100)/number;
        progress(percentage);
        console.log(percentage);
    })

    $.fn.shuffle = function() {

			var allElems = this.get(),
				getRandom = function(max) {
					return Math.floor(Math.random() * max);
				},
				shuffled = $.map(allElems, function(){
					var random = getRandom(allElems.length),
						randEl = $(allElems[random]).clone(true)[0];
					allElems.splice(random, 1);
					return randEl;
			   });

			this.each(function(i){
				$(this).replaceWith($(shuffled[i]));
			});

			return $(shuffled);

    };


});

function text_qs(num){
    for(i=1;i<=num;i++){
        txt = "Question "+i;
        $(".qs-text").eq(i-1).text(txt);
    }
}

function change_qs(i){
    $('.carousel').carousel(i)
    /*
    if(i == number){
        $('#next').attr("disabled", true);
    }
    else if(i == 1){
        $('#prev').attr("disabled", true);
    }
    */
    return false;
}

function prog_count() {
    qs_attempted = $(':radio:checked');
    console.log(qs_attempted)
}

function create(num){
    var x =0,y=0;
    for(var i=0;i<num;i++){
        btn = "<button onclick='change_qs("+i+");return false'  class='btn btn-info rounded-circle mx-2 py-2 px-3 my-2' id='btn-"+i+"'>"+(i+1)+"</button>";
        $("#qs-panel").append(btn);
        if((i+1)%4 == 0){
            $("#use").append("<br>")
        }
    }
}



var x = setInterval(function(){
	timer_no--;

	var minutes = Math.floor(timer_no /60);
	var seconds = Math.floor(timer_no % 60);

	document.getElementById("demo1").innerHTML = minutes + "m " + seconds + "s ";

	if ( timer_no< 0) {
        clearInterval(x);
        document.getElementById("demo1").innerHTML = "EXPIRED";
    }
},1000);


 function progress(num) {
    $(".progress-bar").css("width",''+num+'%');
	$(".progress-bar").text(num+"%");
}

function clear_ans(){
     x = $(".active .qs-text").text();
     var i =x[x.length - 1];
     $('input[name=qs-'+i+']').attr('checked',false);
}

function shuff(num){
     for(var i=1;i<=num;i++){
        $('div#shuffle-'+i+' label').shuffle();
    }
}

function get_current(){
     x = $(".active .qs-text").text();
     var i = x.split(" ")
     return parseInt(i[1])
}