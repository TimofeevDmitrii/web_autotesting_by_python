from soap_functions import checkText_method

def test_missing_letter(word_with_missing_letter):
    response = checkText_method(word_with_missing_letter[0], "ru")
    print(response)
    assert word_with_missing_letter[1] in response[0]['s']


def test_wrong_letter(word_with_wrong_letter):
    response = checkText_method(word_with_wrong_letter[0], "ru")
    print(response)
    assert word_with_wrong_letter[1] in response[0]['s']


