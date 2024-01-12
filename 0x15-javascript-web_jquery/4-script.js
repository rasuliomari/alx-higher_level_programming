$(document).ready(function() {
	$("#toggle_header").click(function() {
		const header = $("header");

                if (header.hasClass("red")) {
                    header.removeClass("red").addClass("green");
                } else {
                    header.removeClass("green").addClass("red");
                }
        });
});
