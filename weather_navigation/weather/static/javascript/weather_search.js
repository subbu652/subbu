const cityInput = document.querySelector(".inpt");
const searchButton = document.querySelector(".btn1");
const locationButton = document.querySelector(".btn2");

const API_KEY = "266eb785a61dca80a994eb215d98dff9";

const getCityCoordinates = async () => {
    const cityName = cityInput.value.trim();
    if (cityName === "") return;
    const API_URL = `https://api.openweathermap.org/geo/1.0/direct?q=${cityName}&limit=1&appid=${API_KEY}`;
    try {
        const response = await fetch(API_URL);
        const data = await response.json();
        if (!data.length) return alert(`No coordinates found for ${cityName}`);
        const { lat, lon, name } = data[0];
        window.location.href = `/weather?city=${name}&lat=${lat}&lon=${lon}`; 
    } catch (error) {
        alert("An error occurred while fetching the coordinates!");
    }
}

const getUserCoordinates = () => {
    navigator.geolocation.getCurrentPosition(
        async position => {
            try {
                const { latitude, longitude } = position.coords;
                const API_URL = `https://api.openweathermap.org/geo/1.0/reverse?lat=${latitude}&lon=${longitude}&limit=1&appid=${API_KEY}`;
                const response = await fetch(API_URL);
                const data = await response.json();
                const { name } = data[0];
                window.location.href = `/weather?city=${name}&lat=${latitude}&lon=${longitude}`;
            } catch (error) {
                alert("An error occurred while fetching the city name!");
            }
        },
        error => {
            if (error.code === error.PERMISSION_DENIED) {
                alert("Geolocation request denied. Please reset location permission to grant access again.");
            } else {
                alert("Geolocation request error. Please reset location permission.");
            }
        }
    );
}

locationButton.addEventListener("click", getUserCoordinates);
searchButton.addEventListener("click", getCityCoordinates);
cityInput.addEventListener("keyup", e => e.key === "Enter" && getCityCoordinates());
