document.addEventListener("DOMContentLoaded", function () {

    var modal = document.getElementById("delete-modal2");
    var modalBody = document.getElementById("modal-body2");
    var closeButton = document.getElementsByClassName("close-button2")[0];


    // Attach click event to each delete button dynamically
    weatherData.forEach(weather => {
        const button = document.getElementById(`myBtn-${weather.city}`);

        if (button) {
            button.addEventListener('click', function (event) {
                event.preventDefault(); // Prevent default link behavior
                console.log(`See more about ${weather.city}`)

                // Set the modal content dynamically based on the city
                modalBody.innerHTML = `
                    <h5>${weather.city}, ${weather.country} , <img src="http://openweathermap.org/img/wn/${weather.icon}.png"> </h5>
                    <p>Lon: ${weather.lon}, Lat: ${weather.lat}</p>
                    <p>Main: ${weather.main}</p><p>Description: ${weather.description}</p>

                    <p>Temp: ${weather.temperature}°C, Feels Like: ${weather.feels_like}°C, Min Temp: ${weather.temp_min}°C, Max Temp: ${weather.temp_max}°C, Min Temp: ${weather.temp_min}°C</p>
                    <p>Pressure: ${weather.pressure} hPa, Humidity: ${weather.humidity}%, Sea Level: ${weather.sea_level} km, Ground level: ${weather.grnd_level} km</p>
                    <p>Visibility: ${weather.visibility} km</p>
                    <p>Wind Speed: ${weather.wind_speed} m/s, Wind Direction: ${weather.wind_deg}°</p>
                    <p>Description: ${weather.description}</p>
                    <p>timezone: ${weather.timezone}</p>
                    <p>Clouds: ${weather.clouds} %</p>
                    
                    <button type="button" onclick="window.location.href='/'" class="btn btn-secondary">Cancel</button>
                `;

                // Display the modal
                modal.style.display = 'block';
            });
        }
    });

    // Close the modal when the close button is clicked
    closeButton.onclick = function () {
        modal.style.display = "none";
    };

    // Close the modal when the user clicks outside the modal
    window.onclick = function (event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };

});