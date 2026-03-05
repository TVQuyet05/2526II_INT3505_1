const express = require("express");
const app = express();
const port = 3000;

// Middleware (JSON parsing)
app.use(express.json());

// In-memory data
let users = [
  { id: 1, name: "Nguyen Van A", email: "a@example.com" },
  { id: 2, name: "Tran Thi B", email: "b@example.com" },
];

// 1. Get List
app.get("/users", (req, res) => res.json(users));

// 2. Get Detail
app.get("/users/:id", (req, res) => {
  const user = users.find((u) => u.id == req.params.id);
  user ? res.json(user) : res.status(404).json({ message: "Not found" });
});

// 3. Create
app.post("/users", (req, res) => {
  const newUser = { id: users.length + 1, ...req.body };
  users.push(newUser);
  res.status(201).json(newUser);
});

// 4. Update Email
app.patch("/users/:id", (req, res) => {
  const user = users.find((u) => u.id == req.params.id);
  if (user) {
    if (req.body.email) user.email = req.body.email;
    res.json(user);
  } else {
    res.status(404).json({ message: "Not found" });
  }
});

// 5. Delete
app.delete("/users/:id", (req, res) => {
  users = users.filter((u) => u.id != req.params.id);
  res.status(204).send();
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
