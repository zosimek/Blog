var owl = $('.owl-carousel');
owl.owlCarousel({
    items: 5,
    margin: 15,
    loop: true,
    autoWidth: true,
    center: true,
    autoplay: true,
    autoplaySpeed: 1000, // move one item every 5 seconds
    slideBy: 1, // move one item at a time
    autoplayHoverPause: true,
});