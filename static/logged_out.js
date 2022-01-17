// Signup Modal
const signup = document.getElementById("signup");
const signupContainer = document.getElementById("signup_container");
const signupOne = document.getElementById("signup_1");
const signupTwo = document.getElementById("signup_2");
const signupThree = document.getElementById("signup_3");
const close = document.getElementById("close");

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
const loginClose = document.getElementById("login_close");
const login = document.getElementById("login")
const loginWindow = document.getElementById("login_window");
const loginContainer = document.getElementById("login_container");

login.addEventListener("click", () => {
  loginWindow.classList.add("show");
  signup.classList.remove("show");
});

signupThree.addEventListener("click", () => {
  modal.classList.add("show");
  loginWindow.classList.remove("show");
});

window.addEventListener('mouseup', function (event) {
  if ((event.target != loginContainer && event.target.parentNode != loginContainer && event.target.parentNode.parentNode != loginContainer) || event.target === loginClose) {
    loginWindow.classList.remove("show");
  }
})

// Password Check
const signupPassword = document.getElementById("signup_password");
const confirmPassword = document.getElementById("confirm_password");
const result = document.getElementById('message');
const submitSignin = document.getElementById("submit_signin")

function checkPassword() {
  if (signupPassword.value === confirmPassword.value) {
    result.innerText = "Passwords match";
    result.classList.add("success");
    submitSignin.disabled = false
  } else {
    result.innerText = "Passwords do not match";
    result.classList.add("alert");
    submitSignin.disabled = true
  }
}

signupPassword.addEventListener("keyup", () => {
  if (confirmPassword.value.length != 0) checkPassword();
});

confirmPassword.addEventListener("keyup", checkPassword);