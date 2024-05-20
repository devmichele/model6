<?php
// Get form data
$name = $_POST['name'];
$email = $_POST['email'];
$message = $_POST['message'];

// Customize email settings
$to = 'mycheelly@gmail.com';
$subject = 'Novo formulário de contato';
$body = "Nome: $name\nEmail: $email\nMensagem: $message";

// Send email
if (mail($to, $subject, $body)) {
    http_response_code(200); // Success
} else {
    http_response_code(500); // Error
}
?>
