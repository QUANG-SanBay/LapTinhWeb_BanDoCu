function isRequire(value) {
    return value.trim() ? undefined : true;
}

function isEmail(value) {
    var regex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return regex.test(value) ? undefined : true;
}

function isRePassWord(valuePass, valueRePass) {
    return valuePass === valueRePass ? undefined : true;
}

function validateField(index, input, errElm, form_gr, form_label, extraParams) {
    var success = true;
    if (isRequire(input.value)) {
        errElm[index].innerText = `vui lòng nhập trường "${form_label[index].innerText}".`;
        form_gr[index].classList.add('invalid');
        success = false;
    }
    else if (form_label[index].innerText === 'Email' && isEmail(input.value)) {
        errElm[index].innerText = `Trường này phải là ${form_label[index].innerText}.`;
        form_gr[index].classList.add('invalid');
        success = false;
    }
    else if (
        extraParams && extraParams.password &&
        form_label[index].innerText === 'Nhập lại mật khẩu' &&
        isRePassWord(extraParams.password.value, input.value)
    ) {
        errElm[index].innerText = `${form_label[index].innerText} không hợp lệ.`;
        form_gr[index].classList.add('invalid');
        success = false;
    } else {
        errElm[index].innerText = '';
        form_gr[index].classList.remove('invalid');
    }
    return success;
}

function attachValidation(FormEl, rules, extraParams) {
    rules.forEach(function(value, index) {
        var errElm = FormEl.querySelectorAll('.form-mess');
        var form_gr = FormEl.querySelectorAll('.form-group');
        var form_label = FormEl.querySelectorAll('.form-label');
        value.onblur = function() {
            if (value.value.trim() !== "" || (extraParams && extraParams.password && form_label[index].innerText === 'Nhập lại mật khẩu')) {
                validateField(index, value, errElm, form_gr, form_label, extraParams);
            }
        }
    });
}

function validateOnSubmit(FormEl, rules, extraParams) {
    var isSuccess = true;
    var errElm = FormEl.querySelectorAll('.form-mess');
    var form_gr = FormEl.querySelectorAll('.form-group');
    var form_label = FormEl.querySelectorAll('.form-label');

    rules.forEach(function(value, index) {
        if (!validateField(index, value, errElm, form_gr, form_label, extraParams)) {
            isSuccess = false;
        }
    });
    return isSuccess;
}