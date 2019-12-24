function openModal() {
    const urlParams = new URLSearchParams(window.location.search);
    let form = urlParams.get('form');
    if (form) {
        $('#' + form + 'Modal').modal('show');
    }
}