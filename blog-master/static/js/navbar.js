const open = document.querySelector(".mob-open");
const close = document.querySelector(".mob-close");

const wrapper = document.querySelector(".mob-wrapper").classList;

function displayNavBar(){
    wrapper.toggle("opened");
    wrapper.toggle("close");
}

open.addEventListener("click", displayNavBar);
close.addEventListener("click", displayNavBar);