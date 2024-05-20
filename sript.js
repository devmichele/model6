document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // Get form values
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    // Create a FormData object and append form data
    var formData = new FormData();
    formData.append('name', name);
    formData.append('email', email);
    formData.append('message', message);

    // Send form data to backend
    fetch('backend.php', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (response.ok) {
            // Optionally, display a success message or redirect the user
            console.log('Form submission successful');
            // Clear form fields
            document.getElementById('name').value = '';
            document.getElementById('email').value = '';
            document.getElementById('message').value = '';
        } else {
            console.error('Form submission failed');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
