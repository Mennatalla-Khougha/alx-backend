import { createQueue } from "kue";

const queue = createQueue();

const blackList = ["4153518780", "4153518781"];

function sendNotification(phoneNumber, msg, job, done) {
	job.progress(0, 100);
	if (blackList.includes(phoneNumber)) {
		done(new Error(`Phone number ${phoneNumber} is blacklisted`));
		return;
	}
	job.progress(50, 100);
	console.log(`Sending notification to ${phoneNumber}, with message: ${msg}`);
	done();
}

queue.process("push_notification_code_2", 2, (job, done) => {
	const { phoneNumber, message } = job.data;
	sendNotification(phoneNumber, message, job, done);
});
