import express from "express";
import { promisify } from "util";
import { createClient } from "redis";

const app = express();

const port = 1245;

const client = createClient();

const listProducts = [
	{ id: 1, name: "Suitcase 250", price: 50, stock: 4 },
	{ id: 2, name: "Suitcase 450", price: 100, stock: 10 },
	{ id: 3, name: "Suitcase 650", price: 350, stock: 2 },
	{ id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(id) {
	return listProducts.find((ele) => ele.id === id);
}

app.get("/list_products", (req, res) => {
	res.json(listProducts);
});

client.on("error", (err) =>
	console.log("Redis client not connected to the server:", err)
);

client.on("ready", () => console.log("Redis client connected to the server"));

function reserveStockById(itemId, stock) {
	client.set(itemId, stock);
}

const getAsync = promisify(client.get).bind(client);

async function getCurrentReservedStockById(itemId) {
	const reply = await getAsync(itemId);
	return reply;
}

app.get("/list_products/:itemId", async (req, res) => {
	const itemId = req.params.itemId;
	const product = getItemById(itemId);

	if (!product) {
		return res.json({ status: "Product not found" });
	}

	const stock = await getCurrentReservedStockById(itemId);
	res.json({
		itemId: product.id,
		itemName: product.name,
		price: product.price,
		initialAvailableQuantity: product.stock,
		currentQuantity: stock !== null ? parseInt(stock) : 0,
	});
});

app.get("/reserve_product/:itemId", async (req, res) => {
	const itemId = req.params.itemId;
	const product = getItemById(itemId);

	if (!product) {
		return res.json({ status: "Product not found" });
	}

	const stock = await getCurrentReservedStockById(itemId);
	if (stock < 1) {
		return res.json({ status: "Not enough stock available", itemId });
	} else {
		reserveStockById(itemId, stock - 1);
		res.json({ status: "Reservation confirmed", itemId });
	}
});

app.listen(port, () => {});
