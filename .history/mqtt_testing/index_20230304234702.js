
// Dầu tiên mấy ông tạo project nodejs 

// sau đó install: npm install mqtt --save

// done

const mqtt = require('mqtt')
client = mqtt.connect({
    host: "io.adafruit.com",
    port: 1883,
    protocol: (parseInt(1883) === 8883 ? 'mqtts' : 'mqtt'),
    username: "dangnguyen",
    password: "aio_jQtu93uvUOlMqTzCH8h4HsniQlvn",
    connectTimeout: 60 * 1000,
    keepalive: 3600
  });

client.on('connect', () => {
    client.subscribe('dangnguyen/feeds/button1/json');
    connected = true;
    console.log('connected');
});

client.on('reconnect', () => {
    client.subscribe('dangnguyen/feeds/button1/json');
    connected = true;
    console.log('connected');
});

client.on('error', (err) => console.log('error', err));

client.on('offline', () => connected = false);

client.on('close', () => connected = false);

client.on('message', (topic, message) => {
    buffer.push(message);
    console.log('message', message);
});
