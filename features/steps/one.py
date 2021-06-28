from behave import step  # noqa
from behave.model import Table


def palindromo_checker(input):
    print(input)
    if (input[0] == input[-1] ):
        #print(input[1:-1])
        size = len(input)
        if size >= 1:
            return True
        return palindromo_checker(input[1:-1])
    else:
        return False

def is_palindrome(texto):
    texto_cap = texto.upper().replace(' ', '')
    return texto_cap == texto_cap[::-1]


def contar_palabras(entrada):
    #empty value
    if str(entrada.strip()) == '\'\'':
        return len(entrada.split(" ")) - 1
    else:
        return len(entrada.split(" "))


def contar_frases(entrada):
    return len(entrada.split(".")) - 1


@step(u'an input text like {texto}')
def entrada(context, texto=None):
    """
    :type context: behave.runner.Context
    """
    context.input = texto


@step(u'the word count is triggered')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = contar_palabras(context.input)


@step("the sentences count is triggered")
def sentence_counter(context):
    """
    :type context: behave.runner.Context
    """
    context.result = contar_frases(context.input)


@step(u'the result should be {expected}')
def create_random_filter_object(context, expected=None):
    """
    :type context: behave.runner.Context
    """
    print("expected {} vs context.result {}".format(expected, context.result))
    assert int(expected) == int(context.result)

@step(u'the palindrome should be {expected}')
def create_random_filter_object(context, expected):
    """
    :type context: behave.runner.Context
    """
    print("expected {} vs context.result {}".format(expected, context.result))
    assert (expected == str(context.result))



@step(u'the palindrome is triggered')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = palindromo_checker(context.input)


@step("the func palindrome is triggered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.result = is_palindrome(context.input)

@step(u'the palindrome output should be {result}')
def step_impl(context, result):
    """
    :type context: behave.runner.Context
    :type result: str
    """
    assert(str(context.result) == result)
