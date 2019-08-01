var fs = require('fs');
var httpServ = require('https');
var WebSocketServer = require('ws').Server;
var alarm;
var app = httpServ.createServer({
    key: fs.readFileSync('/etc/httpd/ssl/3_nussh.happydoudou.xyz.key'),
    cert: fs.readFileSync('/etc/httpd/ssl/2_nussh.happydoudou.xyz.crt')
});

app.listen(8000,function() {
    console.log('server started.')
});

var wss = new WebSocketServer({
    server: app
});

wss.on('connection', function(wsConnect) {
    wsConnect.on('message', function(message) {
        console.log("received ",message);

        if(message=='Cancel'){
            alarm=0
            wsConnect.send('Cancel Received!');    
        }
        else if (message=='Alarm'||alarm==1){
            alarm=1
            wsConnect.send('Alarm');
        }
        else if(message=='Safe'||alarm==0){
            wsConnect.send('Safe');
        }
    });
});

var conn = new WebSocket('wss://nussh.happydoudou.xyz:8000/');
conn.onmessage = function(e){ console.log(e.data); };
conn.onopen = () => conn.send('message');