
// Dầu tiên mấy ông tạo project nodejs 

// sau đó install: npm install mqtt --save

// done

// Login Adafruit: 
    /*
    username: dangnguyen
    pass: Dang1012
    */

feed = [
    "dangnguyen/feeds/button1", 
    "dangnguyen/feeds/button2",
    "dangnguyen/feeds/FanValue",
    "dangnguyen/feeds/LightValue",
    "dangnguyen/feeds/sensor1",
    "dangnguyen/feeds/sensor2"
]

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
    for (const topic in feed){
        client.subscribe(feed[topic]);
        console.log('connected ' + feed[topic]);
    }
    
});

client.on('reconnect', () => {
    client.subscribe('dangnguyen/feeds/button1/json');
    console.log('connected');
});

client.on('error', (err) => console.log('error', err));

client.on('offline', () => connected = false);

client.on('close', () => connected = false);

client.on('message', (topic, message) => {
    console.log('topic\n', topic)
    console.log('message', JSON.stringify(message));
    console.log(message.toString('utf8'));
});

