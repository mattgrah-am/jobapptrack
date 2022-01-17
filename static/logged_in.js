// Add new job Modal
const newJobClose = document.getElementById("newjob_close");
const addNew = document.getElementById("add_new")
const newJobWindow = document.getElementById("newjob_window");
const newJobContainer = document.getElementById("newjob_container");

addNew.addEventListener("click", () => {
  newJobWindow.classList.add("show");
});


window.addEventListener('mouseup', function (event) {
  if ((event.target != newJobContainer && event.target.parentNode != newJobContainer && event.target.parentNode.parentNode != newJobContainer && event.target.parentNode.parentNode.parentNode != newJobContainer && event.target.parentNode.parentNode.parentNode.parentNode != newJobContainer && event.target.parentNode.parentNode.parentNode.parentNode.parentNode != newJobContainer) || event.target === newJobClose) {
    newJobWindow.classList.remove("show");
  }
})