<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8" />
	<title>Inscription</title>
</head>
<body>
	{% extends "base.html"%}
{% block title %} Sign up {% endblock %}
{% block content %}
	{% with messages = get_flashed_messages() %}
		{% if messages %}
			{% for msg in messages %}
				<p>{{msg}}</p>
			{% endfor %}
		{% endif %}
	{% endwith %}
	<h5> Sign in here if you already have an account</h5>
	<form action="/login">
		<button>Log in</button>
	</form>
	<br><br>
	<h5>Sign up here: </h5>
	<form action="#" method="POST">
		<p>Name:</p>
		<p><input type="text" name="nm"/></p>
		<p>Username:</p>
		<p><input type="text" name="usernm"></p>
		<p>Password:</p>
		<p><input type="text" name="passwrd"></p>
		<p><input type="submit" value="Sign up"></p>
	</form>
{% endblock %}	
</body>
</html>
