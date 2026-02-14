<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Interactive Letter</title>
</head>
<body>
    <h1 style="font-size: {{ size }}px;">{{ message }}</h1>

    <img src="/static/images/{{ image }}" width="{{ img_size }}" alt="Letter image">

    <form action="/response" method="post">
        <input type="text" name="user_input" placeholder="Type yes or no" required>
        <input type="hidden" name="size" value="{{ size }}">
        <input type="hidden" name="img_size" value="{{ img_size }}">
        <input type="hidden" name="step" value="{{ step }}">
        <button type="submit">Submit</button>
    </form>
</body>
</html>
