fetch('/', {
    headers: {
        'x-requested-with': 'XMLHttpRequest'
    }
})
.then(response => response.json())
.then(data => {
    const weatherData = data.weather_data;
    weatherData.forEach(function(weather) {
        const city = weather.city; // Replace spaces with hyphens for valid IDs
        // console.log(city)
        const offsetInSeconds = weather.timezone; // Offset in seconds from UTC
        // console.log(offsetInSeconds)
        const offsetInHours = offsetInSeconds / 3600; // Convert seconds to hours
        // console.log(offsetInHours)

        // Use Luxon to calculate local time
        const utcDateTime = luxon.DateTime.utc();
        const localTime = utcDateTime.plus({ seconds: offsetInSeconds }).toFormat('yyyy-MM-dd HH:mm');

        // Display the local time in the HTML
        const localTimeElement = document.getElementById(`local-time-${city}`);
        if (localTimeElement) {
            localTimeElement.textContent = localTime;
        } else {
            console.warn(`Element with ID local-time-${city} not found.`);
        }
    });
});