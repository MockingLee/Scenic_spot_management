$(document).ready() = function () {
    $("#search").bind("click",function () {
        alert(123)
        $.get("search?" + $("#input").val(),function (data) {
            alert(data)
        })
    })
}