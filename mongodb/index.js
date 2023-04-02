const express = require("express");
const mongoose = require("mongoose");

const app = express();

mongoose.connect(
  "mongodb+srv://nguyencharlie:smarthome2023@cluster0.ricdizx.mongodb.net/?retryWrites=true&w=majority",
  { useNewUrlParser: true }
);

const db = mongoose.connection;

db.on("error", console.error.bind(console, "connection error:"));
db.once("open", function () {
  console.log("Connected to database!");
});

const fanSchema = new mongoose.Schema({
  _id: String,
  timestamp: Date,
  status: String,
  value: Number,
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
