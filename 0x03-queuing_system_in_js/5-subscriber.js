import { createClient } from 'redis';

const client = createClient({
  host: '127.0.0.1',
  port: 6379
});

client.on('error', err => console.log('Redis client not connected to the server:', err));

client.on('ready', () => console.log('Redis client connected to the server'));

client.subscribe('holberton school channel');

client.on('message', (ch, msg) => {
  console.log(msg);
  if (msg === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});
