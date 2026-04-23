function contactForm() {
    var show = document.getElementById("contactForm");
    if (show.style.display === "none") {
        show.style.display = "block";
    } else {
        show.style.display = "none";
    }
}
function showAlert(event) {
    event.preventDefault()
    alert("Congratulations! Your message sent successfully!")
}
