const menuBtn = document.getElementById("menu-btn");
const navMenu = document.getElementById("nav-menu");

menuBtn.addEventListener("click", () => {
    navMenu.classList.toggle("active");
});


const navLinks = document.querySelectorAll("nav a");

navLinks.forEach(link => {

    link.addEventListener("click", () => {

        navMenu.classList.remove("active");

    });

});


function sendMessage(event) {

    event.preventDefault();

    alert(
        "Thank you for contacting me! " +
        "The contact form backend will be connected soon."
    );

}
function sendMessage(event) {

    event.preventDefault();

    const name = document.getElementById("contact-name").value;
    const email = document.getElementById("contact-email").value;
    const message = document.getElementById("contact-message").value;

    const subject = encodeURIComponent(
        "Portfolio Contact from " + name
    );

    const body = encodeURIComponent(
        "Name: " + name + "\n" +
        "Email: " + email + "\n\n" +
        "Message:\n" + message
    );

    window.location.href =
        "mailto:chaitanyaallamsetty9121@gmail.com" +
        "?subject=" + subject +
        "&body=" + body;
}