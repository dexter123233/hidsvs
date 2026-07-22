module.exports = (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.status(200).json({
    status: "healthy",
    service: "Zavod Extraction API",
    version: "1.0.0",
    timestamp: new Date().toISOString()
  });
};
