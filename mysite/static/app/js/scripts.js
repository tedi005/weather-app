$(document).ready(function() {
    // messages timeout for 3 seconds
    setTimeout(function() {
        $('.messages').fadeOut('slow');
    }, 3000); // <-- time in milliseconds, 3000 = 3 seconds
});

function formatTime(value) {
    return value < 10 ? '0' + value : value;
}

function updateTime() {
    let currentTime = new Date();
    let hours = currentTime.getHours();
    let minutes = currentTime.getMinutes();
    let seconds = currentTime.getSeconds();
    let ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'

    document.getElementById('hrs').innerHTML = formatTime(hours);
    document.getElementById('min').innerHTML = formatTime(minutes);
    document.getElementById('sec').innerHTML = formatTime(seconds);
    document.getElementById('am').innerHTML = ampm;
}

setInterval(updateTime, 1000);
updateTime(); // initial call to display the time immediately
