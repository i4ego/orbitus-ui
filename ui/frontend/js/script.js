function openPage(page = 1) {
    $(".pages").css("transform", `translateY(-${(page - 1) * 100}%)`);
}