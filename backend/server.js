const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
require('dotenv').config();
const connectDB = require('./utils/db');
const requestRoutes = require('./routes/requests');

const app = express();
connectDB();

app.use(cors());
app.use(bodyParser.json());
app.use('/api/requests', requestRoutes);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Backend running on port ${PORT}`));
