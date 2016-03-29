# -*- coding: utf-8 -*-

# Наше приложение
from cms import login_manager, application, db
from flask.ext.login import UserMixin

class User(UserMixin):
	is_authenticated = True
	is_active = True
	is_anonymous = False

	def __init__(self, _uid, _username):
		self.uid = _uid
		self.username = _username

	def __str__(self):
		return self.username

	def get_id(self):
		return str(self.uid)

	def get_absolute_url(self):
		return "/users/%d" % self.uid

	@staticmethod
	def authenticate(username, password):
		cur = db.connection.cursor()
		cur.execute("SELECT id, username FROM users WHERE username = %s AND password = MD5(%s)", (username, password))
		row = cur.fetchone()
		if row is None:
			return None
		else:
			user = User(int(row[0]), row[1])
			return user

	@staticmethod
	def get(user_id):
		cur = db.connection.cursor()
		cur.execute("SELECT id, username FROM users WHERE id = %s", (int(user_id),))
		row = cur.fetchone()
		user = User(int(row[0]), row[1])
		return user

@login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)
