(function ($) {
    "use strict";

    // Navbar on scrolling
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.navbar').fadeIn('slow').css('display', 'flex');
        } else {
            $('.navbar').fadeOut('slow').css('display', 'none');
        }
    });

     // Scroll to Bottom
     $(window).scroll(function () {
         if ($(this).scrollTop() > 100) {
             $('.scroll-to-bottom').fadeOut('slow');
         } else {
             $('.scroll-to-bottom').fadeIn('slow');
         }
     });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });

    
})(jQuery);
