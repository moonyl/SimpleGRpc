const express = require("express");
const app = express();
const port = 8080;

app.use(express.json());

app.post("/download", (req, res) => {
  const { url } = req.body;
  console.log({ url });
});

app.listen(port, () => {
  console.log(`Web Downloader listening at http:localhost:${port}`);
});
