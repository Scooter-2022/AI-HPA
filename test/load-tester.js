import http from "k6/http";
import { sleep } from "k6"

export let options = {
    vus: 1,
    stages: [
        { target: 50, duration: "60s" },
        { target: 150, duration: "60s" },
        { target: 0, duration: "60s" }
    ]
};

export default function() {
    let response = http.get("http://175.45.192.94:30001/");
    sleep(0.01);
    //sleep(Math.random());
};
