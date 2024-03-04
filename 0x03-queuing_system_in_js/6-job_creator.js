import { createQueue } from "kue";

const queue = createQueue();

const data = {
	phoneNumber: "01231456789",
	message: "This is test msg",
};

const job = queue.create("push_notification_code", data).save((err) => {
	if (!err) {
		console.log(`Notification job created: ${job.id}`);
	}
});

job.on("failed", () => console.log("Notification job failed"));
job.on("complete", () => console.log("Notification job completed"));
