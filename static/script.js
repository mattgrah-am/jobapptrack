// Signup Modal
const signup = document.getElementById("signup");
const signupContainer = document.getElementById("signup_container");
const signupOne = document.getElementById("signup_1");
const signupTwo = document.getElementById("signup_2");
const signupThree = document.getElementById("signup_3");
const close = document.getElementById("close");
const loginClose = document.getElementById("login_close");
const login = document.getElementById("login")
const loginWindow = document.getElementById("login_window");
const loginContainer = document.getElementById("login_container");

signupOne.addEventListener("click", () => {
  signup.classList.add("show");
});
signupTwo.addEventListener("click", () => {
  signup.classList.add("show");
});

window.addEventListener('mouseup', function (event) {
  if ((event.target != signupContainer && event.target.parentNode != signupContainer && event.target.parentNode.parentNode != signupContainer) || event.target === close) {
    signup.classList.remove("show");
  }
})

// Login Modal
login.addEventListener("click", () => {
  loginWindow.classList.add("show");
  signup.classList.remove("show");
});

signupThree.addEventListener("click", () => {
  signup.classList.add("show");
  loginWindow.classList.remove("show");
});

window.addEventListener('mouseup', function (event) {
  if ((event.target != loginContainer && event.target.parentNode != loginContainer && event.target.parentNode.parentNode != loginContainer) || event.target === loginClose) {
    loginWindow.classList.remove("show");
  }
})