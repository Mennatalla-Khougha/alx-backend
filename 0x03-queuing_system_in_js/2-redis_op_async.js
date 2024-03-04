import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient({
  host: '127.0.0.1',
  port: 6379
});

client.on('error', err => console.log('Redis client not connected to the server:', err));

client.on('ready', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

const getAsync = promisify(client.get).bind(client);

async function displaySchoolValue(schoolName) {
  const reply = await getAsync(schoolName).catch((err) => {
    throw new Error;
  });
  console.log(reply);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
