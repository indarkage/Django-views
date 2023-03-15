from django import template


register = template.Library()

@register.filter(name='multiply') # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg): # первый аргумент здесь — это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|multiply:arg
    return str(value) * arg # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон

@register.filter(name='Censor')
def Censor(value, arg):
    prof_words = ['anal', 'anus', 'ballsack', 'blowjob', 'blow job', 'boner', 'clitoris', 'cock', 'cunt', 'dick', 'dildo', 'dyke', 'fag', 'fuck', 'jizz', 'labia', 'muff', 'nigger', 'nigga', 'penis', 'piss', 'pussy', 'scrotum', 'sex', 'shit', 'slut', 'smegma', 'spunk', 'twat', 'vagina', 'wank', 'whore']
    censored = []
    for i in prof_words:
        if i in value:
            censored = value.replace(i, len(i)*arg)
            value= censored
    return value