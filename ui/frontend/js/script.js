let currentPage = 1

function openPage(page = 1) {
    $(`#p${currentPage}`).removeClass("active")
    $(".pages").css("transform", `translateY(-${(page - 1) * 100}%)`);
    $(`#p${page}`).addClass("active")
    currentPage = page
}

function loadFileIntoViewer(viewer, file) {
    fetch(`${file}`)
      .then(response => response.text())
      .then(text => {
        text = text.trim()
        if (text == "") {
            text = "<empty>"
        }
        text = ` ${file.split("/")[file.split("/").length-1]}:\n\n` + text
        $(viewer).text(text);
      });
}

function closeUI() {
    window.location.href = "/api/close"
}

function loaded() {
    loadFileIntoViewer('#fileViewer', '/api/files/lists/ipset-all.txt')
}

window.addEventListener("DOMContentLoaded", loaded)

function updateHardware() {
    fetch("/api/hardware")
    .then(response => response.json())
    .then(data => {
        $("#os").text(data.os)
        $("#cpu").text(data.cpu)
        $("#ram").text(data.ram)
        $("#net").text(data.net)
    })
}
setInterval(() => {
    updateHardware()
}, 2500);