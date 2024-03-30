const express = require("express");
const route = express.Router();
const jwt = require("jsonwebtoken");
const User = require("../db/models/user");
const bcrypt = require("bcrypt");

route.post("/register", async (req, res) => {
  console.log("register hit");
  try {
    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(req.body.password, salt);
    const newUser = new User({
      username: req.body.username,
      email: req.body.email,
      password: hashedPassword,
    });
    const user = await newUser.save();
    const token = jwt.sign({ _id: user._id }, process.env.SECRET_KEY);
    console.log(user, token);
    return res.status(200).json({
      message: "signup succesful",
      token: token,
    });
  } catch (error) {
    console.log(error);
    return res.status(500).json(error.errors);
  }
});



route.post("/login", async (req, res) => {
  console.log("login hit");
  try {
    const user = await User.findOne({ email: req.body.email });
    if (!user) {
      return res.status(404).json("user not found");
    }
    const validPassword = await bcrypt.compare(
      req.body.password,
      user.password
    );
    if (!validPassword) {
      return res.status(400).json("wrong password");
    }
    const token = jwt.sign({ _id: user._id }, process.env.SECRET_KEY);
    return res.status(200).json({
      _id: user._id,
      username: user.username,
      email: user.email,
      token: token,
    });
  } catch (error) {
    return res.status(500).json(error);
  }
});




module.exports = route;
