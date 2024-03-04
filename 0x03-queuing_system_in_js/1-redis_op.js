import { createClient, print } from 'redis';

const client = createClient({
  host: '127.0.0.1',
  port: 6379
});

client.on('error', err => console.log('Redis client not connected to the server:', err));

client.on('ready', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      throw new Error();
    } else {
      console.log(reply);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
