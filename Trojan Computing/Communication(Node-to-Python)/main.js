var http = require("http");
const spawn = require("child_process").spawn;
var fs = require('fs');
//argument = process.argv[2]

http.createServer(function (request, response) {

   // Send the HTTP header 
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/plain'});
   
    //convert image to base64
    function base64_encode(file) {
    	  // read binary data
    	  var bitmap = fs.readFileSync(file);
    	  // convert binary data to base64 encoded string
    	  return new Buffer(bitmap).toString('base64');
     }
    var base64str = base64_encode('Capture.PNG');
    
    //save base64 image in a file
    fs.appendFile('base64.txt', base64str, function (err) {
       if (err) throw err;
       console.log('Saved!');
    });

    //calling python script
    const pythonProcess = spawn('python',["base64toImage.py"]);

}).listen(8088);

// Console will print the message
//console.log('Server running at http://127.0.0.1:8088/');