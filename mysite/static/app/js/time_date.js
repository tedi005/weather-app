    // Get the local time for each city
    weatherData.forEach(function(weather) {
        const city = weather.city;
        const offsetInSeconds = weather.timezone; // Offset in seconds from UTC
        const offsetInHours = offsetInSeconds / 3600; // Convert seconds to hours

        // Use Luxon to calculate local time
        const utcDateTime = luxon.DateTime.utc();
        const localTime = utcDateTime.plus({ hours: offsetInHours }).toFormat('yyyy-MM-dd HH:mm');
        
        // Display the local time in the HTML
        const localTimeElement = document.getElementById(`local-time-${city}`);
        if (localTimeElement) {
            localTimeElement.textContent = localTime;
        }
    });