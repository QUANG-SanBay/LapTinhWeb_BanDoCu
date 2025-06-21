var loginFormElm = document.getElementById('form-2');
var loginEmail = document.getElementById('login-email');
var loginPass = document.getElementById('login-password');
var loginBtn = loginFormElm.querySelector('.form-btn__it');
var loginRules = [
    loginEmail,
    loginPass
];

attachValidation(loginFormElm, loginRules);

loginBtn.addEventListener('click', function(e) {
    e.preventDefault();
    if (validateOnSubmit(loginFormElm, loginRules)) {
        var loginData = {
            Email: loginEmail.value,
            Password: loginPass.value,
        };
        console.log(loginData);
    }
});