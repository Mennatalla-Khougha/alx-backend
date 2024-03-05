const kue = require("kue");
const chai = require("chai");
const expect = chai.expect;
const createPushNotificationsJobs = require("./8-job.js");

describe("createPushNotificationsJobs", () => {
	let queue;

	before(() => {
		queue = kue.createQueue();
		queue.testMode.enter(); // Enter test mode
	});

	afterEach(() => {
		queue.testMode.clear();
	});

	after(() => {
		queue.testMode.exit(); // Exit test mode
	});

	it("should throw an error when jobs is not an array", () => {
		expect(() => createPushNotificationsJobs("not an array", queue)).to.throw(
			Error,
			"Jobs is not an array"
		);
	});

	it("should create jobs in the queue", (done) => {
		const jobs = [
			{ phoneNumber: "1234567890", message: "Test message 1" },
			{ phoneNumber: "0987654321", message: "Test message 2" },
		];

		createPushNotificationsJobs(jobs, queue);

		expect(queue.testMode.jobs).to.have.lengthOf(jobs.length);
		done();
	});

	it("should handle an empty jobs array", () => {
		const jobs = [];
		expect(() => createPushNotificationsJobs(jobs, queue)).to.not.throw();
	});

	it("should create jobs with different data", (done) => {
		const jobs = [
			{ phoneNumber: "5551234567", message: "Different message 1" },
			{ phoneNumber: "5557654321", message: "Different message 2" },
		];

		createPushNotificationsJobs(jobs, queue);

		expect(queue.testMode.jobs).to.have.lengthOf(jobs.length);
		done();
	});
});
