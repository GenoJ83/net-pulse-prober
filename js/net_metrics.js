function calculateJitter(latencies) {
  if (!latencies || latencies.length < 2) return 0;
  let totalDiff = 0;
  for (let i = 1; i < latencies.length; i++) {
    totalDiff += Math.abs(latencies[i] - latencies[i - 1]);
  }
  return Number((totalDiff / (latencies.length - 1)).toFixed(2));
}
function calculateUptime(successCount, totalCount) {
  if (!totalCount) return 100.0;
  return Number(((successCount / totalCount) * 100).toFixed(3));
}
module.exports = { calculateJitter, calculateUptime };
