var http = require("http");
const spawn = require("child_process").spawn;
var fs = require('fs');
argument = process.argv[2]

http.createServer(function (request, response) {

   // Send the HTTP header 
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/plain'});

    console.log(argument)

}).listen(8088);

// Console will print the message
console.log('Server running at http://127.0.0.1:8088/');