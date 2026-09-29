// Wait for the HTML document to fully load
document.addEventListener("DOMContentLoaded", function() {
    
    // Find the message paragraph and the username
    const messageElement = document.getElementById("greetingMessage");
    const username = document.getElementById("username").innerText;
    
    // Get the current hour to determine time of day
    const currentHour = new Date().getHours();
    let timeGreeting = "Good evening";

    if (currentHour < 12) {
        timeGreeting = "Good morning";
    } else if (currentHour < 18) {
        timeGreeting = "Good afternoon";
    }

    // Update the DOM dynamically
    messageElement.innerText = `${timeGreeting}, ${username}! Your secure session is active.`;
});