<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Result</title>
    <!-- Bootstrap CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1>Result</h1>
        <p>Name: {{ name }}</p>
        <p>Email: {{ email }}</p>
        <p>Age: {{ age }}</p>
        <p>Gender: {{ gender }}</p>
        <p>Subscribe to newsletter: {% if subscribe %}Yes{% else %}No{% endif %}</p>
        <p>Interests: {% for interest in interests %}{{ interest }}{% if not loop.last %}, {% endif %}{% endfor %}</p>
    </div>
    <!-- Bootstrap JS (optional) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
