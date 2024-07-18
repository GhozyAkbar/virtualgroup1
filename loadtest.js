import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 100 }, // ramp up to 100 users
    { duration: '1m', target: 100 },  // stay at 100 users for 1 minute
    { duration: '10s', target: 0 },   // ramp down to 0 users
  ],
};

export default function () {
  let res = http.get('http://192.168.65.3:30091/');
  check(res, {
    'status was 200': (r) => r.status == 200,
  });
  sleep(1);
}
