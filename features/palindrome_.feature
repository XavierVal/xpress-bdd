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
