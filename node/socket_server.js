var app = require('http').createServer(handler)
  , io = require('socket.io').listen(app)
  , fs = require('fs')

app.listen(80);

var redis = require('socket.io/node_modules/redis');
var sub = redis.createClient(6379,'192.168.192.128');

//Subscribe to the Redis chat channel
sub.subscribe('chat');

function handler (req, res) {
  fs.readFile(__dirname + '/index.html',
  function (err, data) {
    if (err) {
      res.writeHead(500);
      return res.end('Error loading index.html');
    }

    res.writeHead(200);
    res.end(data);
  });
}

io.sockets.on('connection', function (socket) {
	//Grab message from Redis and send to client
    sub.on('message', function(channel, message){
		console.log('receive redis message:'+message);
        //socket.send(message);
		//io.sockets.emit('news', { hello: 'world' });
		io.sockets.emit('news', message);
    });
	
  //socket.emit('news', { hello: 'world' }); send to the client
  io.sockets.emit('news', { hello: 'world' }); //send to all clients
  socket.on('my other event', function (data) {
    console.log(data);
  });
});