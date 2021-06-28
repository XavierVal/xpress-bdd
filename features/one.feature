Feature: words and dicts


  Scenario Outline: Text splitter
    Given an input text like <texto>
    When the word count is triggered
    Then the result should be <words>
    Examples:
      | texto                  | words |
      | ''                     | 0     |
      | 'blab balla blalal'    | 3     |
      | 'uno'                  | 1     |
      | 'uno dos'              | 2     |
      | '1 2 3 4 5 6 7 8 9 10' | 10    |


  Scenario Outline: sentence splitter
    Given an input text like <texto>
    When the sentences count is triggered
    Then the result should be <sentences>
    Examples:
      | texto                        | sentences |
      | 'blab balla blalal'          | 0         |
      | ''                           | 0         |
      | 'uno. dos'                   | 1         |
      | '1. 2. 3. 4 .5 6 .7 8 9 10.' | 6        |

