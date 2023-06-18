const toTop = document.querySelector("#to-top");
const rootElement = document.documentElement;

function scrollToTop() {
  // Scroll to top logic
  rootElement.scrollTo({
    top: 0,
    behavior: "smooth"
  });
}

window.addEventListener("scroll", () => {
    if(window.pageYOffset > 200){
        toTop.classList.add("active");
        toTop.addEventListener("click",scrollToTop)
    } else {
        toTop.classList.remove("active");
        toTop.addEventListener("click",scrollToTop)
    }
})