$(document).ready(function() {

    $("#img1").on('click', function(){ 
       $("#card1").flip();
       var kobe = {};
       kobe['fname'] = 'Kobe';  
       kobe['lname'] = 'Bryant';  
       console.log(JSON.stringify(kobe));
        $.ajax({
                url: API+'/question4', // url where to submit the request
                async: false, 
                type : "POST", // type of action POST || GET
                dataType : 'json', // data type
                contentType:'application/json; charset=utf-8',
                data : JSON.stringify(kobe),// post data || get data
                
                success : function(result) {                   
                    console.log(result);
                    var item =  JSON.parse(result);
                    var player = '<ul class=\"list-group\" id=\"player1\">';
                   console.log(item.points );      
                player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"PPG: "+
                item.points.toFixed(2) + '</li>' + '<br/>';
                 player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"RPG: "+
                item.rebound.toFixed(2) + '</li>' + '<br/>';
                player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"APG: "+
                item.assist.toFixed(2) + '</li>' + '<br/>';
                   
                   player += '</ul>';
                   document.getElementById("kobeinfo").innerHTML = player; 

                },
                error: function(xhr, resp, text) {
                    console.log(xhr, resp, text);
                }
        });
       
     });

    $("#img2").on('click', function(){        
       $("#card2").flip(); 
       var carter = {};
       carter['fname'] = 'Vince';  
       carter['lname'] = 'Carter';  
       console.log(JSON.stringify(carter));
           $.ajax({
                url: API+'/question4', // url where to submit the request
                async: false, 
                type : "POST", // type of action POST || GET
                dataType : 'json', // data type
                contentType:'application/json; charset=utf-8',
                data : JSON.stringify(carter),// post data || get data
                
                success : function(result) {                   
                    console.log(result); 
                    var item =  JSON.parse(result);
                    var player = '<ul class=\"list-group\" id=\"player2\">';
                   console.log(item.points );      
                player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"PPG: "+
                item.points.toFixed(2) + '</li>' + '<br/>';
                 player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"RPG: "+
                item.rebound.toFixed(2) + '</li>' + '<br/>';
                player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"APG: "+
                item.assist.toFixed(2) + '</li>' + '<br/>';
                   
                   player += '</ul>';
                   document.getElementById("carterinfo").innerHTML = player;
                },
                error: function(xhr, resp, text) {
                    console.log(xhr, resp, text);
                }
        });
       
     });
    $("#img3").on('click', function(){   
       $("#card3").flip(); 
        var jordan = {};
       jordan['fname'] = 'Michael';  
       jordan['lname'] = 'Jordan';  
           $.ajax({
                url: API+'/question4', // url where to submit the request
                async: false, 
                type : "POST", // type of action POST || GET
                dataType : 'json', // data type
                contentType:'application/json; charset=utf-8',
                data : JSON.stringify(jordan),// post data || get data
                
                success : function(result) {                   
                    console.log(result); 
                    var item =  JSON.parse(result);
                    var player = '<ul class=\"list-group\" id=\"player3\">';
                   console.log(item.points );      
                player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"PPG: "+
                item.points.toFixed(2) + '</li>' + '<br/>';
                 player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"RPG: "+
                item.rebound.toFixed(2) + '</li>' + '<br/>';
                player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"APG: "+
                item.assist.toFixed(2) + '</li>' + '<br/>';
                   
                   player += '</ul>';
                   document.getElementById("jordaninfo").innerHTML = player;
                },
                error: function(xhr, resp, text) {
                    console.log(xhr, resp, text);
                }
        });
       
     });
    $("#img4").on('click', function(){   
       $("#card4").flip(); 
       var iverson = {};
       iverson['fname'] = 'Allen';  
       iverson['lname'] = 'Iverson';  
           $.ajax({
                url: API+'/question4', // url where to submit the request
                async: false, 
                type : "POST", // type of action POST || GET
                dataType : 'json', // data type
                contentType:'application/json; charset=utf-8',
                data : JSON.stringify(iverson),// post data || get data
                
                success : function(result) {                   
                    console.log(result); 
                    var item =  JSON.parse(result);
                    var player = '<ul class=\"list-group\" id=\"player4\">';
                   console.log(item.points );      
                player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"PPG: "+
                item.points.toFixed(2) + '</li>' + '<br/>';
                 player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"RPG: "+
                item.rebound.toFixed(2) + '</li>' + '<br/>';
                player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"APG: "+
                item.assist.toFixed(2) + '</li>' + '<br/>';
                   
                   player += '</ul>';
                   document.getElementById("iversoninfo").innerHTML = player;
                },
                error: function(xhr, resp, text) {
                    console.log(xhr, resp, text);
                }
        });
       
     });

	var qid;
    var qid2;
    var API = 'http://127.0.0.1:5000';
    var players;
	$("#questions").change(function() {
         qid = $(this).find('option:selected').attr('id');
         //console.log(qid);
    });
    $("#questionType2").change(function() {
         qid2 = $(this).find('option:selected').attr('id');
         console.log(qid2);
    });
    var submitArray = {};
    var type1 = 1;
    var type2 = 2;

    $("#searchbtn").on('click', function(){
         
         submitArray['qid'] = qid;
         //submitArray['type'] = type1;
         console.log(JSON.stringify(submitArray));

    $.ajax({
                url: API+'/question1', // url where to submit the request
                async: false, 
                type : "POST", // type of action POST || GET
                dataType : 'json', // data type
                contentType:'application/json; charset=utf-8',
                data : JSON.stringify(submitArray),// post data || get data
                
                success : function(result) {
                    // you can see the result from the console
                    // tab of the developer tools
                    
                    console.log(result);
                    var playerInfo = '<ul class=\"list-group\" id=\"playerInfo\">';
                    jQuery.each(JSON.parse(result), function(i, item) {
                        
                         playerInfo +=
                '<li class=\"list-group-item list-group-item-info\"  >' +
                item.fname + " "+ item.lname + '</li>' + '<br/>';
                
                    console.log(item.lname);
                    });
                   playerInfo += '</ul>';
                   console.log(playerInfo);
                   // console.log(result.getJSONArray("fname"));
                   document.getElementById("playerInfo").innerHTML = playerInfo; 
                },
                error: function(xhr, resp, text) {
                    console.log(xhr, resp, text);
                }
        });
     });
    
    
    var submit3 = {};
    $("#type3btn").on('click', function(){                 
        submit3['fname'] = $('#playerFname').val();  
        submit3['lname'] = $('#playerLname').val();  
   
        console.log(JSON.stringify(submit3));
        $.ajax({
                url: API+'/question3', // url where to submit the request
                async: false, 
                type : "POST", // type of action POST || GET
                dataType : 'json', // data type
                contentType:'application/json; charset=utf-8',
                data : JSON.stringify(submit3),// post data || get data
                
                success : function(result) {
                    
                    var res = '<ul class=\"list-group\" id=\"type3res\">';
                    var item = JSON.parse(result);
                    console.log(item.points.toFixed(2));

                    res +=
                '<li class=\"list-group-item list-group-item-info\"  >' +"In Year"+" "+
                item.year + " "+ submit3['fname']+ " "+ " may get "+ item.points.toFixed(2) + 
                " points per game based on our machine learning prediction"+'</li>' + '<br/>';
                    res += '</ul>';
                    document.getElementById("playerInfo3").innerHTML = res; 
                    console.log(res);
                   
                },
                error: function(xhr, resp, text) {
                    console.log(xhr, resp, text);
                }
        });

    });


    var submit4 = {};
    $("#type4btn").on('click', function(){                 
        submit4['fname'] = $('#playerfname').val();  
        submit4['lname'] = $('#playerlname').val();  
   
        console.log(JSON.stringify(submit4));
        $.ajax({
                url: API+'/question4', // url where to submit the request
                async: false, 
                type : "POST", // type of action POST || GET
                dataType : 'json', // data type
                contentType:'application/json; charset=utf-8',
                data : JSON.stringify(submit4),// post data || get data
                
                success : function(result) {
                   
                    console.log(result);
                    var item =  JSON.parse(result);
                    var player = '<ul class=\"list-group\" id=\"type4question\">';
                   console.log(item.points );      
                player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"PPG: "+
                item.points.toFixed(2) + '</li>' + '<br/>';
                 player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"RPG: "+
                item.rebound.toFixed(2) + '</li>' + '<br/>';
                player +=
                '<li class=\"list-group-item list-group-item-info\"  \
                style=\"height: 30px; padding: 5px 15px;\">' +"APG: "+
                item.assist.toFixed(2) + '</li>' + '<br/>';
                   
                   player += '</ul>';
                   document.getElementById("playerInfo4").innerHTML = player;
                   
                },
                error: function(xhr, resp, text) {
                    console.log(xhr, resp, text);
                }
        });

    });
    


    
});






