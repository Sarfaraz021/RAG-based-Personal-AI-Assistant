require("dotenv").config();
const express = require("express");
const cors = require("cors");
const connect_DB = require("./db/db");

const authRoute = require("./routes/auth");


const app = express();
app.use(cors());
app.use(express.json());

app.use("/api/auth", authRoute);


const port = process.env.PORT
app.listen(port ,async () => {
  await connect_DB();
  console.log("Server running on port 3000");
});
