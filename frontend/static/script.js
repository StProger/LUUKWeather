let host;

if (window.location.hostname === "localhost") {
    host = "http://localhost:8000";
}

function get_weather(){

    const url = `${host}/weather`;
    return fetch(url);
}