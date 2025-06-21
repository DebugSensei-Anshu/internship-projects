// === server.js ===

const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(bodyParser.json());

let posts = [];

// Get all posts
app.get("/posts", (req, res) => {
    res.json(posts);
});

// Create new post
app.post("/posts", (req, res) => {
    const { title, content } = req.body;
    const id = posts.length + 1;
    posts.push({ id, title, content });
    res.status(201).json({ message: "Post created successfully" });
});

// Delete post
app.delete("/posts/:id", (req, res) => {
    const id = parseInt(req.params.id);
    posts = posts.filter(post => post.id !== id);
    res.json({ message: "Post deleted successfully" });
});

const PORT = 5000;
app.listen(PORT, () => console.log(`Server running at http://localhost:${PORT}`));
