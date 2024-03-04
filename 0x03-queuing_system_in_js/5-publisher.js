import { createClient } from 'redis';

const client = createClient({
  host: '127.0.0.1',
  port: 6379
});

client.on('error', err => console.log('Redis client not connected to the server:', err));

client.on('ready', () => console.log('Redis client connected to the server'));

function publishMessage (msg, time) {
  setTimeout(() => {
    console.log(`About to send ${msg}`);
    client.publish('holberton school channel', msg);
  }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
