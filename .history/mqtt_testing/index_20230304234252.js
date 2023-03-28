
// Dầu tiên mấy ông tạo project nodejs 

// sau đó install: npm install mqtt --save

// done

const mqtt = require('mqtt')
client = mqtt.connect({
    host: "io.adafruit.com",
    port: 1883,
    protocol: (parseInt(port) === 8883 ? 'mqtts' : 'mqtt'),
    username: "dangnguyen",
    password: "aio_jQtu93uvUOlMqTzCH8h4HsniQlvn",
    connectTimeout: 60 * 1000,
    keepalive: 3600
  });

  client.on('connect', () => {
    client.subscribe('dangnguyen/feeds/button1/json');
    connected = true;
    emit('connected');
  });

  client.on('reconnect', () => {
    client.subscribe('dangnguyen/feeds/button1/json');
    connected = true;
    emit('connected');
  });

  client.on('error', (err) => emit('error', err));

  client.on('offline', () => connected = false);

  client.on('close', () => connected = false);

  client.on('message', (topic, message) => {
    buffer.push(message);
    emit('message', message);
  });



client.on('connect', function () {
  client.subscribe('presence', function (err) {
    if (!err) {
      client.publish('presence', 'Hello mqtt')
    }
  })
})

client.on('message', function (topic, message) {
  // message is Buffer
  console.log(message.toString())
  client.end()
})