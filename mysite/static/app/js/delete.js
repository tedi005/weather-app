
document.addEventListener("DOMContentLoaded", function() {
    const DateTime = luxon.DateTime;
    const modal = document.getElementById("delete-modal");
    const modalBody = document.getElementById("modal-body");
    const closeButton = document.getElementsByClassName("close-button")[0];
   

    // Loop over the weather data passed from Django

    // Iterate over the weather data
    weatherData.forEach(function (weather) {
        const city = weather.city;
        const deleteButton = document.getElementById(`delete-button-${city}`);

        if (deleteButton) {
            deleteButton.addEventListener("click", function (event) {
                event.preventDefault(); // Prevent default link behavior
                console.log(`Want to delete ${weather.city}?`)

                // Generate the delete URL dynamically
                const deleteUrl = deleteUrlTemplate.replace("city_placeholder", city);

                // Set the modal content
                modalBody.innerHTML = `
                    <h3>Are you sure you want to delete ${city}?</h3>
                    <form action="${deleteUrl}" method="post" style="display:inline;">
                        <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
                        <button type="submit" class="btn btn-danger">Confirm</button>
                        <button type="button" onclick="window.location.href='/'" class="btn btn-secondary">Cancel</button>
                    </form>
                `;

                // Display the modal
                modal.style.display = "block";
            });
        }
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

