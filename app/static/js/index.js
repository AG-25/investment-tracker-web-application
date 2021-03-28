$(".fas-logged-in").on("click", function() {
    $(".search-path").hide()
    setTimeout(addSearch, 100);
});

function addSearch() {
    $(".new-form").show(500);
}