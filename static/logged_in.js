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


// Edit job Modal
const editJobClose = document.getElementById("editjob_close");
const editjob = document.getElementById("editjob")
const editJobWindow = document.getElementById("editjob_window");
const editJobContainer = document.getElementById("editjob_container");

addNew.addEventListener("click", () => {
  editJobWindow.classList.add("show");
});


window.addEventListener('mouseup', function (event) {
  if ((event.target != editJobContainer && event.target.parentNode != editJobContainer && event.target.parentNode.parentNode != editJobContainer && event.target.parentNode.parentNode.parentNode != editJobContainer && event.target.parentNode.parentNode.parentNode.parentNode != editJobContainer && event.target.parentNode.parentNode.parentNode.parentNode.parentNode != editJobContainer) || event.target === editJobClose) {
    editJobWindow.classList.remove("show");
  }
})