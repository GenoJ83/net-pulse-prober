const { calculateJitter, calculateUptime } = require('../../js/net_metrics');

describe('Network Metrics', () => {
  it('computes mean consecutive jitter', () => {
    const data = [10, 15, 12, 18];
    const jitter = calculateJitter(data);
    expect(jitter).toBeGreaterThan(0);
  });
  it('calculates three-decimal SLA uptime percentage', () => {
    expect(calculateUptime(999, 1000)).toBe(99.9);
  });
});
