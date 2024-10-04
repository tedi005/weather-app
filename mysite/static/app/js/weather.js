// document.addEventListener("DOMContentLoaded", function() {
//     const DateTime = luxon.DateTime;

//     var modal = document.getElementById("delete-modal");
//     var modalBody = document.getElementById("modal-body");
//     var closeButton = document.getElementsByClassName("close-button")[0];

//     // Attach click event to each delete button
//     {% for weather in weather_data %}
//         (function(city) {
//             document.getElementById('delete-button-{{ weather.city }}').addEventListener('click', function(event) {
//                 event.preventDefault(); // Prevent default link behavior
//                 // Set the modal content
//                 modalBody.innerHTML = `
//                     <h2>Are you sure you want to delete ${city}?</h2>
//                     <form action="{% url 'delete' weather.city %}" method="post" style="display:inline;">
//                         {% csrf_token %}
//                         <button type="submit" class="btn btn-danger">Confirm</button>
//                         <button type="button" onclick="window.location.href='{% url 'index' %}'" class="btn btn-secondary">Cancel</button>
//                     </form>
//                 `;
//                 // Display the modal
//                 modal.style.display = 'block';
//             });
//         })("{{ weather.city }}");
//     {% endfor %}

//     // Close the modal when the close button is clicked
//     closeButton.onclick = function() {
//         modal.style.display = "none";
//     }

//     // Close the modal when the user clicks outside the modal
//     window.onclick = function(event) {
//         if (event.target == modal) {
//             modal.style.display = "none";
//         }
//     }

//     // Get the weather data from Django
//     const weatherData = {{ weather_data|safe }};

//     function getLocalTime(timezoneOffset) {
//         const now = new Date();
//         // Convert timezone offset from seconds to milliseconds
//         const localTime = new Date(now.getTime() + timezoneOffset * 1000);
//         return localTime.toLocaleString();
//     }

//     weatherData.forEach(weather => {
//         const city = weather.city;
//         const offsetInHours = weather.timezone / (60 * 60); // offset in seconds from UTC
//         const zone = offsetInHours > 0 ? `UTC+${offsetInHours}` : `UTC${offsetInHours}`;

//         const localTime = DateTime.utc().setZone(zone).toFormat('yyyy-MM-dd HH:mm');

//         // Set the local time for each city
//         document.getElementById(`local-time-${city}`).textContent = localTime;

//         console.log("City:", city);
//         console.log(`Local time for ${city}:`, localTime);
//     });
// });



document.addEventListener("DOMContentLoaded", function() {
    const DateTime = luxon.DateTime;

    var modal = document.getElementById("delete-modal");
    var modalBody = document.getElementById("modal-body");
    var closeButton = document.getElementsByClassName("close-button")[0];

    // Attach click event to each delete button
    const weatherData = JSON.parse(document.getElementById('weather-data').textContent);
    weatherData.forEach(weather => {
        const city = weather.city;
        document.getElementById(`delete-button-${city}`).addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior
            // Set the modal content
            modalBody.innerHTML = `
                <h2>Are you sure you want to delete ${city}?</h2>
                <form action="/delete/${city}" method="post" style="display:inline;">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${document.querySelector('[name=csrfmiddlewaretoken]').value}">
                    <button type="submit" class="btn btn-danger">Confirm</button>
                    <button type="button" onclick="window.location.href='/index/'" class="btn btn-secondary">Cancel</button>
                </form>
            `;
            // Display the modal
            modal.style.display = 'block';
        });
    });

    // Close the modal when the close button is clicked
    closeButton.onclick = function() {
        modal.style.display = "none";
    };

    // Close the modal when the user clicks outside the modal
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };

    // Function to get local time
    function getLocalTime(timezoneOffset) {
        const now = new Date();
        const localTime = new Date(now.getTime() + timezoneOffset * 1000);
        return localTime.toLocaleString();
    }

    weatherData.forEach(weather => {
        const city = weather.city;
        const offsetInHours = weather.timezone / (60 * 60); // offset in seconds from UTC
        const zone = offsetInHours > 0 ? `UTC+${offsetInHours}` : `UTC${offsetInHours}`;
        const localTime = DateTime.utc().setZone(zone).toFormat('yyyy-MM-dd HH:mm');

        document.getElementById(`local-time-${city}`).textContent = localTime;
    });
});








// document.addEventListener("DOMContentLoaded", function() {
//     const DateTime = luxon.DateTime;

//     var modal = document.getElementById("delete-modal");
//     var modalBody = document.getElementById("modal-body");
//     var closeButton = document.getElementsByClassName("close-button")[0];

//     // Attach click event to each delete button
//     const weatherData = JSON.parse(document.getElementById('weather-data').textContent);
//     weatherData.forEach(weather => {
//         const city = weather.city;
//         document.getElementById(`delete-button-${city}`).addEventListener('click', function(event) {
//             event.preventDefault(); // Prevent default link behavior
//             // Set the modal content
//             modalBody.innerHTML = `
//                 <h2>Are you sure you want to delete ${city}?</h2>
//                 <form action="/delete/${city}" method="post" style="display:inline;">
//                     <input type="hidden" name="csrfmiddlewaretoken" value="${csrftoken}">
//                     <button type="submit" class="btn btn-danger">Confirm</button>
//                     <button type="button" onclick="window.location.href='/index/'" class="btn btn-secondary">Cancel</button>
//                 </form>
//             `;
//             // Display the modal
//             modal.style.display = 'block';
//         });
//     });

//     // Close the modal when the close button is clicked
//     closeButton.onclick = function() {
//         modal.style.display = "none";
//     };

//     // Close the modal when the user clicks outside the modal
//     window.onclick = function(event) {
//         if (event.target == modal) {
//             modal.style.display = "none";
//         }
//     };

//     // Get the weather data from Django
//     function getLocalTime(timezoneOffset) {
//         const now = new Date();
//         const localTime = new Date(now.getTime() + timezoneOffset * 1000);
//         return localTime.toLocaleString();
//     }

//     weatherData.forEach(weather => {
//         const city = weather.city;
//         const offsetInHours = weather.timezone / (60 * 60); // offset in seconds from UTC
//         const zone = offsetInHours > 0 ? `UTC+${offsetInHours}` : `UTC${offsetInHours}`;
//         const localTime = DateTime.utc().setZone(zone).toFormat('yyyy-MM-dd HH:mm');

//         document.getElementById(`local-time-${city}`).textContent = localTime;
//     });
// });
