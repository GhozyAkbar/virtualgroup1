import http from 'k6/http';
import { check, sleep } from 'k6';
import { Trend } from 'k6/metrics';

export let options = {
  stages: [
    { duration: '30s', target: 100 }, // ramp up to 100 users
    { duration: '1m', target: 100 },  // stay at 100 users for 1 minute
    { duration: '10s', target: 0 },   // ramp down to 0 users
  ],
  thresholds: {
    'http_req_duration': ['p(95)<500'], // 95% of requests must complete below 500ms
  },
  ext: {
    loadimpact: {
      projectID: 1234567,
      name: "Load Test",
    },
    influxdb: {
      url: 'http://localhost:8086/k6',
      organization: '',
      token: '',
      bucket: '',
    },
  },
};

export default function () {
  let res = http.get('http://192.168.65.3:30081/');
  check(res, {
    'status was 200': (r) => r.status == 200,
  });
  sleep(1);
}
