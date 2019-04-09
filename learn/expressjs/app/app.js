var express = require('express');
var reload = require('reload');
var io = require('socket.io')();
var app = express();
var dataFile = require('./data/data.json');

app.set('port', process.env.PORT || 3000);
app.set('appData', dataFile);
app.set('view engine', 'ejs');
app.set('views', 'app/views');

app.locals.siteTitle = 'FJD';

app.use(express.static('app/public'));
app.use(require('./routes/index'));
app.use(require('./routes/speakers'));
app.use(require('./routes/api'));

var server = app.listen(app.get('port'), function() {
    console.log('Listening on port ' + app.get('port'));
});
io.attach(server);
io.on('connection',function(socket){
	console.log('User connected');
	
});
reload(server, app);
// var http = require('http');

// var myServer = http.createServer(function (req,res){
// 	res.writeHead(200,{"Content-Type":"text/html"});
// 	res.write('<h1>asjda</h1>');
// 	res.end();
// });

// myServer.listen(3000);
// console.log('Server is running at http://localhost:3000')