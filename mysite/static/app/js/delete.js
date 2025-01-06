document.addEventListener("DOMContentLoaded", function() {
    // const DateTime = luxon.DateTime;
    const modal = document.getElementById("delete-modal");
    const modalBody = document.getElementById("modal-body");
    const closeButton = document.getElementsByClassName("close-button")[0];

    // Fetch weather data dynamically
    fetch('/', {
        headers: {
            'x-requested-with': 'XMLHttpRequest'
        }
    })
    .then(response => response.json())
    .then(data => {
        const weatherData = data.weather_data;

        // Iterate over the weather data
        weatherData.forEach(function (weather) {
            const city = weather.city;
            const deleteButton = document.getElementById(`delete-button-${city}`);

            if (deleteButton) {
                deleteButton.addEventListener("click", function (event) {
                    event.preventDefault(); // Prevent default link behavior
                    console.log(`Want to delete ${weather.city}?`);

                    // Generate the delete URL dynamically
                    const deleteUrl = deleteUrlTemplate.replace("city_placeholder", city);

                    // Set the modal content
                    modalBody.innerHTML = `
                        <h3>Are you sure you want to delete ${city}?</h3>
                        <form action="${deleteUrl}" method="post" style="display:inline;">
                            <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                            <button type="submit" class="btn btn-danger">Confirm</button>
                            <button type="button" class="btn btn-secondary close-modal">Cancel</button>
                        </form>
                    `;

                    // Display the modal
                    modal.style.display = "block";

                    // Attach event listener to the cancel button within the modal
                    modal.querySelector('.close-modal').addEventListener('click', function() {
                        modal.style.display = "none";
                    });
                });
            }
        });

    })
    .catch(error => {
        console.error('Error fetching weather data:', error);
    });

    // Close the modal when the close button is clicked
    closeButton.onclick = function() {
        modal.style.display = "none";
    }

    // Close the modal when the user clicks outside the modal
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
});
