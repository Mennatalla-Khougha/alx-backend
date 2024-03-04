import { createQueue } from "kue";

const queue = createQueue();

function sendNotification(phoneNumber, msg) {
	console.log(`Sending notification to ${phoneNumber}, with message: ${msg}`);
}

queue.process("push_notification_code", (job, done) => {
	sendNotification(job.data.phoneNumber, job.data.message);
	done();
});
