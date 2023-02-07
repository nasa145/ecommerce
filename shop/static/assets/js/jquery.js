
//The code to work wiyh product description and product reviews abiluty to move and load inside a div
//by hidin the other content and showing the rest
// ths code is found at the product detaul page inside the shop app
$(document).ready(function(){
    $('#product-review-link').click(function(){
        $("#product-desc-tab").removeClass("show active");
        $("#product-review-tab").addClass("show active");
    });
});

$(document).ready(function(){
    $('#product-desc-link').click(function(){
        $('#product-review-tab').removeClass("show active");
        $('#product-desc-tab').addClass("show active");
    })
});


// the code to work with accounts and for the login and signup
//found at the account app at login.html
$(document).ready(function(){
    $('#signin-tab-2').click(function(){
        $('#register-2').removeClass("show active");
        $('#signin-2').addClass("show active");
    });
});

$(document).ready(function(){
    $('#register-tab-2').click(function(){
        $('#signin-2').removeClass("show active");
        $('#register-2').addClass("show active");
    });
});






