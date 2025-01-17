document.addEventListener("DOMContentLoaded", function () {
    fetch('/', {
        headers: {
            'x-requested-with': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        var modal = document.getElementById("delete-modal2");
        var modalBody = document.getElementById("modal-body2");
        var closeButton = document.getElementsByClassName("close-button2")[0];

        const weatherData = data.weather_data;
        // console.log(weatherData);
        weatherData.forEach(weather => {
            const button = document.getElementById(`myBtn-${weather.city}`);
            if (button) {
                button.addEventListener('click', function (event) {
                    event.preventDefault();
                    // console.log(`See more about ${weather.city}`);
                    modalBody.innerHTML = `
                        <h5>${weather.city}, ${weather.country} , <img src="http://openweathermap.org/img/wn/${weather.icon}.png"> </h5>
                        <p>Lon: ${weather.lon}, Lat: ${weather.lat}</p>
                        <p>Main: ${weather.main}</p><p>Description: ${weather.description}</p>
                        <p>Temp: ${weather.temperature}°C, Feels Like: ${weather.feels_like}°C, Min Temp: ${weather.temp_min}°C, Max Temp: ${weather.temp_max}°C</p>
                        <p>Pressure: ${weather.pressure} hPa, Humidity: ${weather.humidity}%, Sea Level: ${weather.sea_level} km, Ground level: ${weather.grnd_level} km</p>
                        <p>Visibility: ${weather.visibility} km</p>
                        <p>Wind Speed: ${weather.wind_speed} m/s, Wind Direction: ${weather.wind_deg}°</p>
                        <p>timezone: ${weather.timezone}</p>
                        <p>Clouds: ${weather.clouds} %</p>
                        <button type="button" onclick="window.location.href='/'" class="btn btn-outline-dark">Cancel</button>
                    `;
                    modal.style.display = 'block';
                });
            } else {
                console.warn(`Button not found for city: ${weather.city}`);
            }
        });
        if (closeButton) {
            closeButton.onclick = function() {
                modal.style.display = "none";
            };
        } else {
            console.warn("Close button not found in the DOM.");
        }

        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        };
    })
    .catch(error => {
        console.error('Error fetching weather data:', error);
    });
});
