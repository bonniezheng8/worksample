<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="asg7.css">
        <link href="https://fonts.googleapis.com/css?family=Arvo|Oxygen|Source+Sans+Pro|Berkshire+Swash|Exo+2:800" rel="stylesheet">
        <title> Web Development 2019 </title>
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">
        <!-- jQuery library -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        <!-- Latest compiled JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>

    </head>
    
    <body onload="setInterval('chat.update()', 1000)">

        <nav class="navbar navbar-default navstyle">
              <div class="container-fluid">
                <ul class="nav navbar-nav">
                    <li><a href="index.html"> <img src="images/b.png" alt="B" style="width:55px"> </a></li>
                  <li><a href="about.html"> <img src="images/eleph.svg" alt="Elephant" style="width:50px"> About Me</a></li>
                  <li><a href="js1.html"><img src="images/lion.svg" alt="Lion" style="width:50px"> Javascript 1</a></li>
                  <li><a href="js2.html"><img src="images/hippo.svg" alt="Hippo" style="width:50px"> Javascript 2</a></li>
                  <li><a href="js3.html"><img src="images/dog.svg" alt="Dog" style="width:50px"> Javascript 3</a></li>
                  <li><a href="jQuery.html"><img src="images/monkey.svg" alt="Monkey" style="width:50px"> jQuery</a></li>
                  <li><a href="asg6.php"><img src="images/turtle.svg" alt="Turtle" style="width:50px"> PHP</a></li>
                  <li><a href="asg7.php"><img src="images/giraffe.svg" alt="Giraffe" style="width:50px"> AJAX</a></li>
                  <li><a href="extra.html"><img src="images/cow.svg" alt="Cow" style="width:50px"> Firebase</a></li>
                </ul>
              </div>
        </nav>
        
        
        <div id="wholename">
        
            <h2 class="title">Join the chat!</h2>
            <div id="namebox">
                Enter your name: <input type="text" id="name">
                <button onclick="myFunction()" id="button"> Chat! </button>
            </div>
        </div>

        <div id="wholechat" style="display: none;">
            
            <h2 class="title">Chat with me!</h2>

            <p id="name-area"></p>
            <a href="asg7.php" id="logout">Change name</a>

            <div id="chat-wrap">
                <div id="chat-area">
                </div>
            </div>

            <form id="send-message-area">
                <p>Your message: </p>
                <textarea id="sendie" maxlength = '100' ></textarea>
            </form>

        </div>

        <script type="text/javascript" src="asg7.js"></script>
        <script type="text/javascript">
            
            var name = "Guest";
            function myFunction(){

                var tempName = document.getElementById("name").value;
                // strip tags
                tempName = tempName.replace(/(<([^>]+)>)/ig,"");

                if (tempName.length > 0) {
                    name = tempName;
                }

                var wholename = document.getElementById("wholename");
                var wholechat = document.getElementById("wholechat");

                wholechat.style.display = 'block';
                wholename.style.display = 'none';

                // display name on page
                $("#name-area").html("You are: <span>" + name + "</span>");

            }


            // kick off chat
            var chat =  new Chat();
            $(function() {

                 chat.getState(); 

                 // watch textarea for key presses
                 $("#sendie").keydown(function(event) {  

                     var key = event.which;  

                     //all keys including return.  
                     if (key >= 33) {

                         var maxLength = $(this).attr("maxlength");  
                         var length = this.value.length;  

                         // don't allow new content if length is maxed out
                         if (length >= maxLength) {  
                             event.preventDefault();  
                         }  
                      }
                 });
                
                 // watch textarea for release of key press
                 $('#sendie').keyup(function(e) {	

                      if (e.keyCode == 13) { 

                        var text = $(this).val();
                        var maxLength = $(this).attr("maxlength");  
                        var length = text.length; 

                        // send 
                        if (length <= maxLength + 1) { 

                            chat.send(text, name);	
                            $(this).val("");

                        } else {
                            $(this).val(text.substring(0, maxLength));
                        }	
                      }
                 });

            });
        </script>
        
</body>

</html>