$('#form-expertise-all').click(function (event) {
    if (this.checked) {
        $('#form-expertise-art').each(function () {
            this.checked = true;
        });
        $('#form-expertise-literature').each(function () {
            this.checked = true;
        });
        $('#form-expertise-science').each(function () {
            this.checked = true;
        });
        $('#form-expertise-entertainment').each(function () {
            this.checked = true;
        });
    } else {
        $('#form-expertise-art').each(function () {
            this.checked = false;
        });
        $('#form-expertise-literature').each(function () {
            this.checked = false;
        });
        $('#form-expertise-science').each(function () {
            this.checked = false;
        });
        $('#form-expertise-entertainment').each(function () {
            this.checked = false;
        });
    }
});

$('#form-content-all').click(function (event) {
    if (this.checked) {
        $('#form-content-title').each(function () {
            this.checked = true;
        });
        $('#form-content-content').each(function () {
            this.checked = true;
        });
    } else {
        $('#form-content-title').each(function () {
            this.checked = false;
        });
        $('#form-content-content').each(function () {
            this.checked = false;
        });
    }
});