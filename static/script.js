window.addEventListener("load", (event) => {
	link = window.location.pathname;
	lang_link = link.split('/')[1];
	img = document.querySelector('img.img-language');
	a = document.querySelector('a.a-language');
	if (lang_link === 'en'){
		a_link = link.replace('en', 'ru');
		a.href = a_link;
		img.src = '/static/language2.jpg';
	}
	else{
		a_link = link.replace('ru', 'en');
		a.href = a_link;
		img.src = '/static/language.png';
	}
});