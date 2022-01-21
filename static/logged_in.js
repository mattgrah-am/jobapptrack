// Add new job Modal
const newJobClose = document.getElementById("newjob_close");
const addNew = document.getElementById("add_new")
const newJobWindow = document.getElementById("newjob_window");
const newJobContainer = document.getElementById("newjob_container");

addNew.addEventListener("click", () => {
  newJobWindow.classList.add("show");
});

window.addEventListener('mouseup', function (event) {
  if (!event.target.closest("#newjob_container") || event.target.matches("#newjob_close")) {
    newJobWindow.classList.remove("show");
  }
})

// Edit job Modal
const editJobClose = document.getElementById("editjob_close");
const editjob = document.querySelectorAll(".edit")
const editJobWindow = document.getElementById("editjob_window");
const editJobContainer = document.getElementById("editjob_container");

editjob.forEach(el => el.addEventListener("click", () => {
  editJobWindow.classList.add("show");
}));

window.addEventListener('mouseup', function (event) {
  if (!event.target.closest("#editjob_container") || event.target.matches("#editjob_close")) {
    editJobWindow.classList.remove("show");
  }
})