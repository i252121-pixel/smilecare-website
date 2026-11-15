document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('.contact-form');
    
    if (form) {
        form.addEventListener('submit', function (event) {
            const messageField = document.getElementById('message');
            
            if (messageField) {
                // Strip out < and > characters to prevent raw HTML/JS tags from submitting
                messageField.value = messageField.value.replace(/[<>]/g, '');
            }
        });
    }
});
