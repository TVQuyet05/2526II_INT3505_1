const express = require("express");
const swaggerJsdoc = require("swagger-jsdoc");
const swaggerUi = require("swagger-ui-express");

const app = express();
const PORT = 3000;

app.use(express.json());

// ==========================================
// SWAGGER CONFIGURATION
// ==========================================
const swaggerOptions = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "Simple HTTP Demo API",
      version: "1.0.0",
      description: "A minimal API to demonstrate HTTP Methods and Status Codes",
    },
    servers: [{ url: `http://localhost:${PORT}` }],
  },
  apis: [__filename], // Read default JSDoc from this file
};

const swaggerDocs = swaggerJsdoc(swaggerOptions);
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerDocs));

// ==========================================
// 1. DEMO HTTP METHODS (CRUD)
// ==========================================
let todos = [
  { id: 1, title: "Learn HTTP" },
  { id: 2, title: "Practice Coding" },
];

/**
 * @swagger
 * components:
 *   schemas:
 *     Todo:
 *       type: object
 *       properties:
 *         id:
 *           type: integer
 *         title:
 *           type: string
 */

/**
 * @swagger
 * /todos:
 *   get:
 *     summary: Get all todos
 *     tags: [Todos]
 *     responses:
 *       200:
 *         description: List of todos
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 $ref: '#/components/schemas/Todo'
 */
app.get("/todos", (req, res) => res.json(todos));

/**
 * @swagger
 * /todos:
 *   post:
 *     summary: Create a new todo
 *     tags: [Todos]
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               title:
 *                 type: string
 *     responses:
 *       201:
 *         description: Created
 */
app.post("/todos", (req, res) => {
  const newTodo = { id: Date.now(), title: req.body.title || "Untitled" };
  todos.push(newTodo);
  res.status(201).json(newTodo);
});

/**
 * @swagger
 * /todos/{id}:
 *   put:
 *     summary: Update a todo entirely
 *     tags: [Todos]
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               title:
 *                 type: string
 *     responses:
 *       200:
 *         description: Updated
 *       404:
 *         description: Not Found
 */
app.put("/todos/:id", (req, res) => {
  const idx = todos.findIndex((t) => t.id == req.params.id);
  if (idx < 0) return res.status(404).json({ error: "Not Found" });
  todos[idx] = { id: Number(req.params.id), title: req.body.title };
  res.json(todos[idx]);
});

/**
 * @swagger
 * /todos/{id}:
 *   delete:
 *     summary: Delete a todo
 *     tags: [Todos]
 *     parameters:
 *       - in: path
 *         name: id
 *         required: true
 *         schema:
 *           type: integer
 *     responses:
 *       204:
 *         description: No Content
 */
app.delete("/todos/:id", (req, res) => {
  todos = todos.filter((t) => t.id != req.params.id);
  res.sendStatus(204);
});

// ==========================================
// 2. DEMO HTTP STATUS CODES
// ==========================================

/**
 * @swagger
 * /status/{code}:
 *   get:
 *     summary: Test any HTTP Status Code
 *     tags: [Status Codes]
 *     parameters:
 *       - in: path
 *         name: code
 *         required: true
 *         description: The HTTP status code to return (e.g., 200, 404, 500)
 *         schema:
 *           type: integer
 *     responses:
 *       '200':
 *         description: Successful operation
 *       '400':
 *         description: Invalid status code
 *       '404':
 *         description: Not Found example
 *       '500':
 *         description: Server Error example
 */
// Endpoint động để test bất kỳ status code nào: GET /status/404, /status/500...
app.all("/status/:code", (req, res) => {
  const code = parseInt(req.params.code);

  // Một số code đặc biệt cần xử lý header
  if (code === 301 || code === 302) {
    return res.redirect(code, "/todos");
  }

  if (code >= 100 && code < 600) {
    res.status(code).json({
      status: code,
      message: `Đây là phản hồi với HTTP Status Code ${code}`,
    });
  } else {
    res.status(400).json({ error: "Invalid status code" });
  }
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
  console.log(`Swagger UI available at http://localhost:${PORT}/api-docs`);
});
