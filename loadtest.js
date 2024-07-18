import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 100 },
    { duration: '1m', target: 100 },
    { duration: '10s', target: 0 },
  ],
  thresholds: {
    'http_req_duration': ['p(95)<500'],
  },
  ext: {
    influxdb: {
      // URL harus sesuai dengan konfigurasi InfluxDB di Docker Compose
      // Jika menggunakan IP lokal Docker, pastikan menggunakan IP yang benar
      url: 'http://influxdb:8086/k6', // InfluxDB URL
      token: '', // InfluxDB token, kosongkan jika tidak memerlukan token
      org: '', // Organisasi di InfluxDB, kosongkan jika tidak memerlukan organisasi
      bucket: '', // Bucket di InfluxDB, kosongkan jika tidak memerlukan bucket
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
