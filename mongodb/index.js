// Cài Mongoose: npm install --save mongoose
// Cài ExpressJS: npm install express

// Using ExpressJS (1)
const express = require("express");
const { Decimal128 } = require("mongodb");
// Using ExpressJS (2)
const app = express();

// Bước tiếp theo, chúng ta sẽ tiến hành kết nối với MongoDB.
const mongoose = require("mongoose");
mongoose.connect(
  "mongodb+srv://nguyencharlie:smarthome2023@cluster0.ricdizx.mongodb.net/?retryWrites=true&w=majority",
  { useNewUrlParser: true }
);

// Chúng ta có một kết nối đang chờ xử lý đến cơ sở dữ liệu trên MongoDB Atlas (Server Singapore).
// Bây giờ, cần bắt được sự kiện nếu chúng ta kết nối thành công hoặc nếu xảy ra lỗi kết nối:
const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));
db.once("open", function () {
  console.log("Connected to database!");
});
const { Schema } = mongoose;

// Tạo Schema:
const fanSchema = new mongoose.Schema({
  _id: String,
  //General Attributes.
  fanID: String,
  status: String,
  //Private Attributes.
  timestamp: Date,
  value: Number,
});

const bulbSchema = new mongoose.Schema({
  _id: String,
  //General Attributes.
  bulbID: String,
  status: String,
  //Private Attributes.
  timestamp: Date,
  value: Number,
});

const tempSchema = new mongoose.Schema({
  _id: String,
  //General Attributes.
  tempID: String,
  timestamp: Date,
  //Private Attributes.
  temp: Decimal128,
});

const lightSchema = new mongoose.Schema({
  _id: String,
  //General Attributes.
  lightID: String,
  timestamp: Date,
  //Private Attributes.
  light: Decimal128,
});

const doorSchema = new mongoose.Schema({
  _id: String,
  //General Attributes.
  doorID: String,
  timestamp: Date,
  //Private Attributes.
  status: String,
});

const userSchema = new mongoose.Schema({
  _id: String,
  userID: String,
  Fname: String,
  Lname: String,
  Email: String,
  Password: String,
  dateOfBirth: Date,
  PhoneNumber: Number,
});

const userCommandSchema = new mongoose.Schema({});

const homeSchema = new mongoose.Schema({
  _id: String,
  Key: Number,
  HomeID: String,
  Address: [{ HomeNumber: Number, Street: String, City: String }],
});

const roomSchema = new mongoose.Schema({
  _id: String,
  roomID: String,
});

const Fan = mongoose.model("Fan", fanSchema, "Fan");
console.log("true");

Fan.find({})
  .exec()
  .then((data) => {
    console.log(data);
  })
  .catch((err) => {
    console.log(err);
  });
// app.get('/fans', function(req, res) {
//     Fan.find({}, function(err, data) {
//       if (err) {
//         console.log(err);
//         res.status(500).send('Error retrieving data');
//       } else {
//         console.log(data);
//         res.send(data);
//       }
//     });
//   });

app.listen(3000, function () {
  console.log("Server running on port 3000");
});

console.log("true");
