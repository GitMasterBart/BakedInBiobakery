let primaryNav = document.querySelector('.primary-navigation');
let navToggle = document.querySelector(".mobile-nav-toggle");

navToggle.addEventListener('click', () => {
    let visibility = primaryNav.getAttribute('data-visible')
    let expanded = navToggle.getAttribute('aria-expanded')

    if ( visibility === "false") {
        primaryNav.setAttribute("data-visible", true);
        navToggle.setAttribute('aria-expanded', true);
    } else{
    primaryNav.setAttribute('data-visible', false);
    navToggle.setAttribute('aria-expanded' , false);}


});


const buttons = document.querySelectorAll("[data-carousel-button]")

buttons.forEach(button => {
    button.addEventListener("click", () => {
        const offset = button.dataset.carouselButton === "next" ? 1 : -1
        const slides = button
            .closest("[data-carousel]")
            .querySelector("[data-slides]")

        const activeSlide = slides.querySelector("[data-active]")
        let newIndex = [...slides.children].indexOf(activeSlide) + offset
        if (newIndex < 0) newIndex = slides.children.length - 1
        if (newIndex >= slides.children.length) newIndex = 0

        slides.children[newIndex].dataset.active = true
        delete activeSlide.dataset.active
    })
})


const userCardTemplate = document.querySelector("[data-user-template]")
const userCardContainer = document.querySelector("[data-user-cards-container]")
const searchInput = document.querySelector("[data-search]")

let users = []

searchInput.addEventListener("input", e => {
    const value = e.target.value.toLowerCase()
    users.forEach(user => {
        const isVisible =
            user.name.toLowerCase().includes(value) ||
            user.email.toLowerCase().includes(value)
        user.element.classList.toggle("hide", !isVisible)
    })
})

fetch("https://jsonplaceholder.typicode.com/users")
    .then(res => res.json())
    .then(data => {
        users = data.map(user => {
            const card = userCardTemplate.content.cloneNode(true).children[0]
            const header = card.querySelector("[data-header]")
            const body = card.querySelector("[data-body]")
            header.textContent = user.name
            body.textContent = user.email
            userCardContainer.append(card)
            return { name: user.name, email: user.email, element: card }
        })
    })


let slideshow = document.querySelector(".slide");


let nextImageDelay = 30;
let currentImagecounter = 0;

slideshow[currentImagecounter].style.display = 'block';

setInterval(nextImage, nextImageDelay)
function nextImage() {
    slideshow[currentImagecounter].style.display = 'none';
    currentImagecounter = (currentImagecounter + 1) % slideshow.length;
    slideshow[currentImagecounter].style.display = 'block';
}
