Feature: Add Beneficiary and Transfer Money
  As a registered banking user
  I want to manage beneficiaries and transfer funds securely
  So that I can send money instantly

  Background:
    Given the user is logged into the mobile banking app
    And the user is on the Add Beneficiary screen

  Scenario: Add beneficiary with valid details
    When the user enters account number "123456789012"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the Add Beneficiary button
    Then a success notification "Beneficiary added successfully" is displayed

  Scenario: Add beneficiary with invalid account number
    When the user enters account number "ABC123XYZ"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the Add Beneficiary button
    Then an error message "Account number must be numeric and 10-16 digits" is shown

  Scenario: Transfer money requires OTP verification
    Given a beneficiary "John Doe" with account number "123456789012" exists
    And the user is on the Transfer Money screen
    When the user selects beneficiary "John Doe"
    And the user enters transfer amount "5000"
    And the user clicks Proceed
    Then an OTP is sent to the registered mobile number
    When the user enters an incorrect OTP three times
    Then the transaction is cancelled with error "OTP verification failed"

  Scenario Outline: Add beneficiary with edge case account lengths
    When the user enters account number "<account>"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the Add Beneficiary button
    Then a success notification is displayed

    Examples:
      | account          |
      | 1234567890       |
      | 1234567890123456 |
