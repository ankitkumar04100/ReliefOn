const express = require('express');
const router = express.Router();
const { addRequest, getRequests } = require('../controllers/requestsController');

router.post('/', addRequest);
router.get('/', getRequests);

module.exports = router;
