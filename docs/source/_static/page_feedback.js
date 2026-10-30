// "Did you find what you were looking for?" widget at the bottom of each page.
// Clicks are logged to Simple Analytics as the "rfdpoly_page_feedback" event.
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".page-feedback").forEach(function (widget) {
    widget.querySelectorAll(".page-feedback-button").forEach(function (button) {
      button.addEventListener("click", function () {
        if (typeof window.sa_event === "function") {
          window.sa_event("rfdpoly_page_feedback", {
            helpful: button.dataset.helpful,
            page: widget.dataset.page,
          });
        }
        widget.querySelector(".page-feedback-question").hidden = true;
        widget.querySelector(".page-feedback-buttons").hidden = true;
        widget.querySelector(".page-feedback-thanks").hidden = false;
      });
    });
  });
});
