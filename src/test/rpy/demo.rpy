define a = Character("甲",who_font=Gunshihei.ttf,who_color=#055584,who_outlines=[(absolute(1), "#ffffff", absolute(0), absolute(0))])

define b = Character("乙",who_font=Gunshihei.ttf,who_color=#055584,who_outlines=[(absolute(1), "#ffffff", absolute(0), absolute(0))])

label start:

	a "hello world!"

	b "hello world!"

	a "hello world!"

	$ renpy.movie_cutscene('video/a.ovg')

	$ renpy.movie_cutscene('video/a.ovg')

label start2:

	$ renpy.movie_cutscene('video/b.ovg')

