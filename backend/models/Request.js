const mongoose = require('mongoose');

const RequestSchema = new mongoose.Schema({
    name: String,
    location: {
        lat: Number,
        lon: Number
    },
    category: String,
    description: String,
    status: { type: String, default: 'pending' },
    createdAt: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Request', RequestSchema);
