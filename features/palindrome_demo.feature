Feature: Palindrome checker function
  As user of the palindrome checker
  I want to validate if a text can be a palindrome or not

  Scenario Outline: Palindrome function checker
    Given an input text like <texto>
    When the func palindrome is triggered
    Then the palindrome output should be <result>

    Examples:
      | texto                                                       | result |
      | 'no_es'                                                     | False  |
      | '0123'                                                      | False  |
      | 'racecar'                                                   | True   |
      | 'a'                                                         | True   |
      | ''                                                          | True   |
      | '1'                                                         | True   |
      | 'xxx'                                                       | True   |
      | 'aaa'                                                       | True   |
      | 'palindrome_emordnilap'                                     | True   |
      | 'Abuttuba'                                                  | True   |
      | 'A car a man a maraca'                                      | True   |
      | 'A dog a plan a canal pagoda'                               | True   |
      | 'A dog A panic in a pagoda'                                 | True   |
      | 'A lad named E Mandala'                                     | True   |
      | 'A man a plan a canal Panama'                               | True   |
      | 'A man a plan a cat a ham a yak a yam a hat a canal Panama' | True   |
      | 'A new order began a more Roman age bred Rowena'            | True   |
      | 'A nut for a jar of tuna'                                   | True   |
      | 'A Santa at Nasa'                                           | True   |
      | 'A Santa dog lived as a devil God at NASA  '                | True   |
      | 'A slut nixes sex in Tulsa'                                 | True   |
      | 'A tin mug for a jar of gum Nita'                           | True   |
      | 'Able was I ere I saw Elba'                                 | True   |
      | 'Acrobats stab orca'                                        | True   |
      | 'Aerate pet area'                                           | True   |
      | 'Ah Satan sees Natasha'                                     | True   |
      | 'Air an aria'                                               | True   |
      | 'Al lets Della call Ed Stella '                             | True   |
      | 'alula'                                                     | True   |
      | 'Amen icy cinema'                                           | True   |
      | 'A Toyota! Race fast safe car! A Toyota!'                   | False  |
      | 'A Toyota’s a Toyota'                                       | False  |
      | '*Aibohphobia*'                                             | True   |
      | 'fear of palindromes'                                       | False  |