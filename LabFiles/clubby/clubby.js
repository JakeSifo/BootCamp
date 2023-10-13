http = require('http');

console.log("Loading web application module.");

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.write('Hello World.')

    if (req.url === "/throw") {
        throw "Something bad happened";
    }

    res.end();
}).listen(8000);
