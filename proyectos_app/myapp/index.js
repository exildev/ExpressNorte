var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var motorizados = [];
var empresas = [];
var db = require('pg');
var config = require('./config.json');
console.log(config);
var connectionString = "postgres://"+config.postgres.user+":"+config.postgres.password+"@"+config.postgres.host+"/"+config.postgres.db;
var clients = {};

db.connect(connectionString, function(err, client, done) {
  if(err) {
    return console.error('error fetching client from pool', err);
  }
  client.query('select * from domicilios_pedidows as pws where pws.despachado=false ', '', function(err, result) {
    //call `done()` to release the client back to the pool
    done();

    if(err) {
      return console.error('error running query', err);
    }
    //console.log(result.rows);
    var pedidos = result.rows;
    for(var x in pedidos){
        console.log(pedidos[x].empresa_id);
        client.query('select * from domicilios_empleado where empresa_id=$1 and cargo=$2', [pedidos[x].empresa_id,'MOTORIZADO'], function(err, result) {
          //call `done()` to release the client back to the pool
          done();

          if(err) {
            return console.error('error running query', err);
          }
          console.log(result.rows);

          //output: 1
        });
    }
      console.log("finalizo el evento");
    //output: 1
  });
});


function validarArray(x,array){
  for(var i;i < array.length ; i++){
    if(x == array[i].motorizado){
      return i;
    }
  }
  return -1;
}
function validarExistencia(x,array){
  for(var i;i < array.length ; i++){
    if(x == array[i].motorizado){
      return true;
    }
  }
  return false;
}

io.on('connection', function(socket) {
  socket.on('i-am', function(type) {
  	clients[socket.id] = type;
  	if (type == 'WEB'){
		io.to(socket.id).emit('you-are', socket.id);
		console.log("I AM WEB: " + socket.id);
  	}else
  	if (type == 'CELL'){
  		console.log("I AM CEL: " + socket.id);
  		socket.on('ionic-qr', function(msg){
  			console.log('QR:');
  			console.log(msg);
			io.to(msg.web_id).emit('ionic-qr', msg.cell_id);
		});
		socket.on('send-gps', function(msg){
  			console.log('GPS:');
  			console.log(msg);
  			for (var i in clients){
  				if (clients[i] == 'WEB'){
					io.to(i).emit('send-gps', msg);
  				}
  			}
		});
  	}
  });
  socket.on('hola',function(data){
    console.log(data);
    console.log(data.web_id+"  "+socket.id);
    io.to(socket.id).emit('respuesta', {id_gps:'7845652456'});
  });

  socket.on('motorizado',function(data){
    if(data.identificador_gps === undefined && data.emp_id){
      var res = validarArray(data.motorizado,motorizados);
      if (res > 0){
        motorizados.remove(res);
      }
      motorizados.push({'id':socket.id,'empresa_id':data.empresa_id,'motorizado':data.motorizado});
      io.to(socket.id).emit('respuesta_mot', {estado:true});
    }else{
      io.to(socket.id).emit('respuesta_mot', {estado:false});
    }
  });

  socket.on('pedido_asignado',function(data){
    if(data.motorizado !== undefined && data.empresa_id !== undefined){
        var pos = validarArray(data.motorizado,motorizados);
        if(pos > 0){
          /*proceso de asignacion de pedido definir */
          io.to(motorizados[pos].id).emit('asignar_motorizado',{pedido:data.id_pedido});
          io.to(socket.id).emit('respuesta_pedido_asignado', {estado:true});
        }else{
          io.to(socket.id).emit('respuesta_pedido_asignado', {estado:false});
        }
    }else{
      io.to(socket.id).emit('respuesta_pedido_asignado', {estado:false});
    }
  });

  socket.on('identificar_emp',function(data){
    console.log(data);
    var res = validarArray(data.motorizado,empresas);
    if (res > 0){
      empresas.remove(res);
    }
    empresas.push({'id':socket.id,'web_id':data.web_id,'motorizado':data.motorizado});
    /*Complementar codigo para integracion de respuesta del morizado a el app*/
    io.to(socket.id).emit('resp_identificacion', {id_gps:'7845652456'});
  });
});


app.get('/', function(req, res){
  res.sendFile(__dirname + '/web.html');
});

app.get('/jquery.js', function(req, res){
  res.sendFile(__dirname + '/jquery.js');
});
app.get('/jquery.qrcode.js', function(req, res){
  res.sendFile(__dirname + '/jquery.qrcode.js');
});


app.get('/cell', function(req, res){
  res.sendFile(__dirname + '/cell.html');
});


http.listen(3000, function(){
  console.log('listening on *:3000');
});
