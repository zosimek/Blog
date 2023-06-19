$('.nav-a-search-img').on('click', function () {
    var section1 = $('.section1');
    if (section1.is(':visible')) {
        section1.hide('slow');
    } else {
        section1.show('slow');
    }
});