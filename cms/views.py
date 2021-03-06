# -*- coding: utf-8 -*-

#------------------------------------------#
# Этот файл является частью CMS Cirno v9.0 #
# © 2016 https://github.com/WST            #
# Распространяется на условиях MIT License #
#-------------------------------------------

# Наше приложение
from cms import site

# Flask
from flask import render_template, url_for
from flask.ext.login import login_required

# Werkzeug
from werkzeug.exceptions import abort

# Python
import random

@site.application.route('/')
def home_page():
	cursor = site.db.cursor()
	cursor.execute("SELECT * FROM posts ORDER BY published_at DESC")
	posts = cursor.fetchall()
	return render_template('home-page.htt', title = u'Главная страница', posts = posts)

@site.application.route('/posts/<post_slug>')
def post_page(post_slug):
	cursor = site.db.cursor()
	cursor.execute("SELECT * FROM posts WHERE slug = %s", (post_slug,))
	if cursor.rowcount == 1:
		post = cursor.fetchone()
		return render_template('post-page.htt', title = '')
	else:
		abort(404)
